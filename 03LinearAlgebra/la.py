# -*- coding: utf-8 -*-

__author__ = 'dddd'


from vector import *

from line import *


def testVector():
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])


    v3 = Vector([7.119, 8.215])
    v4 = Vector([-8.223, 0.878])

    scalar = 7.41
    v5 = Vector([1.671, -1.012, -0.318])

    print v1.plus(v2)
    print v3.minus(v4)
    print v5.scalarMultply(scalar)

    print '----------------------------------------'


    v6 = Vector([-0.221, 7.437])
    v7 = Vector([8.813, -1.331, -6.247])

    v8 = Vector([5.581, -2.136])
    v9 = Vector([1.996, 3.108, -4.554])

    print v6.magnitude()
    print v7.magnitude()


    print v8.normalized()
    print v9.normalized()


    print '----------------------------------------'

    v10 = Vector([7.887,4.138])
    v11 = Vector([-8.802, 6.776])

    print v10.dotProducts(v11)

    v12 = Vector( [-5.955, -4.904, -1.874])
    v13 = Vector([-4.496, -8.755, 7.103])

    print v12.dotProducts(v13)

    v14 = Vector([3.183, -7.627])
    v15 = Vector([-2.668, 5.319])

    print v14.includedAngle(v15)

    v16 = Vector([7.35, 0.221, 5.188])
    v17 = Vector([2.751, 8.259, 3.985])

    print v16.includedAngle(v17, True)


    print '----------------------------------------'
    v18 = Vector([-7.579, -7.88])
    v19 = Vector([22.737, 23.64])

    v20 = Vector([-2.029, 9.97, 4.172])
    v21 = Vector([-9.231, -6.639, -7.245])

    v22 = Vector([-2.328, -7.284, -1.214])
    v23 = Vector([-1.821, 1.072, -2.94])


    v24 = Vector([2.118, 4.827])
    v25 = Vector([0, 0])

    print v18.checkParallel(v19)
    print v20.checkParallel(v21)
    print v22.checkParallel(v23)
    print v24.checkParallel(v25)

    print v18.checkOrthogonal(v19)
    print v20.checkOrthogonal(v21)
    print v22.checkOrthogonal(v23)
    print v24.checkOrthogonal(v25)

    print '----------------------------------------'

    v26 = Vector([3.039, 1.879])
    v27 = Vector([0.825, 2.036])

    v28 = Vector([-9.88, -3.264, -8.159])
    v29 = Vector([-2.155, -9.353, -9.473])

    v30 = Vector([3.009, -6.172, 3.692, -2.51])
    v31 = Vector([6.404, -9.144, 2.759, 8.718])

    print v26.project(v27)
    print v28.ortho(v29)

    print v30.project(v31)
    print v30.ortho(v31)

    print '----------------------------------------'

    v26 = Vector([8.462, 7.893, -8.187])
    v27 = Vector([6.984, -5.975, 4.778])

    cp = v26.crossProducts(v27)
    print cp
    print cp.checkOrthogonal(v26)
    print cp.checkOrthogonal(v27)


    v28 = Vector([-8.987, -9.838, 5.031])
    v29 = Vector([-4.268, -1.861, -8.866])

    print v28.paralArea(v29)

    v30 = Vector([1.5, 9.547, 3.691])
    v31 = Vector([-6.007, 0.124, 5.772])

    print v30.triangleArea(v31)

    print '----------------------------------------'


def testLine():


    line1 = Line ([4.046, 2.836], 1.21)
    line2 = Line ([10.115, 7.09], 3.025)

    line3 = Line ([7.204, 3.182], 8.68)
    line4 = Line ([8.172, 4.114], 9.883)

    line5 = Line ([1.182,5.562], 6.744)
    line6 = Line ([1.773, 8.343], 9.525)



    print line1
    print line2
    print line3
    print line4


if __name__ == '__main__':
#    testVector()

    testLine()

