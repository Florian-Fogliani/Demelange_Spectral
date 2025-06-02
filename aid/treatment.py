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
    epoch = 1000
    alpha = 0.01

    M = np.zeros(len(dic))
    for k in range(epoch):
        grad_M = -2 * D.T @ (O - D @ M) + 2 * lam * M
        M = M - alpha * grad_M
        M = np.maximum(M, 0)

    return M
