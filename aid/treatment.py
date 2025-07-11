from aid.config import *


def least_square(dic, sig):
    return sp.optimize.lsq_linear(dic.data, sig).x


def least_square_nn(dic, sig):
    return sp.optimize.nnls(dic.data, sig)[0]


def tikhonov(dic, lam, sig):
    tik = np.eye(len(dic))
    return np.linalg.inv(dic.data.T @ dic.data + lam*tik.T @ tik) @ (dic.data.T @ sig)


def tikhonov_nn(dic, lam, sig):
    D = dic.data
    O = sig
    epoch = 5000
    alpha = 0.9/np.max(np.linalg.eigvals(D.T @ D + 2*lam)
                       )  # Le rayon spectrale
    M = np.zeros(len(dic))
    for k in range(epoch):
        grad_M = -2 * D.T @ (O - D @ M) + 2 * lam * M
        M = M - alpha * grad_M
        M = np.maximum(M, 0)
    return M


def lasso_nn(dic, lam, sig):
    D = dic.data
    O = sig
    epoch = 5000
    alpha = 0.9/np.max(np.linalg.eigvals(D.T@D))  # Le rayon spectrale
    M = np.zeros(len(dic))
    for k in range(epoch):
        grad_M = -D.T @ (O - D @ M) + lam
        M = M - alpha * grad_M
        M = np.maximum(M, 0)

    return M


def lasso_nn_sum(dic, lam, mu, sig):
    D = dic.data
    O = sig
    epoch = 20000
    threshold = 1E-8
    alpha = 0.9/np.max(np.linalg.eigvals(D.T@D + 2*mu))  # Le rayon spectrale
    M = np.ones(len(dic))/len(dic)
    for k in range(epoch):
        grad_M = D.T @ (D @ M - O) + lam + 2*mu*(np.sum(M) - 1)
        new_M = M - alpha * grad_M
        new_M = np.maximum(new_M, 0)
        if np.linalg.norm(new_M - M)/np.linalg.norm(M) < threshold:
            return new_M
        M = new_M
    return M
