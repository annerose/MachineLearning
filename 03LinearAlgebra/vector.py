# -*- coding: utf-8 -*-
import math
from decimal import Decimal, getcontext

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            # 转为双精度
            #self.coordinates = tuple([Decimal(i) for i in coordinates])

            self.coordinates = tuple( coordinates )
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v1):
        if len(self.coordinates) == len(v1.coordinates) :
            arr = []
            for i in range(len(self.coordinates)):
                arr.append(self.coordinates[i] + v1.coordinates[i])

            return Vector(arr)

        return None

    def minus(self, v1):
        if len(self.coordinates) == len(v1.coordinates) :
            arr = []
            for i in range(len(self.coordinates)):
                arr.append(self.coordinates[i] - v1.coordinates[i])

            return Vector(arr)

        return None

    def scalarMultply(self, saclar):

        arr = []
        for i in  self.coordinates:
            arr.append(i * saclar)

        return Vector(arr)


    # 返回向量的长度
    def magnitude(self):

        squartsum = 0
        for i in  self.coordinates  :
            squartsum += (i ** 2)

        return math.sqrt(squartsum)

    # 向量的方向
    def normalized(self):

        mag = self.magnitude()

        if mag != 0 :
            return self.scalarMultply (1.0 / mag)

        return None


    def dotProducts(self, v1):
        if len(self.coordinates) == len(v1.coordinates) :
            dp = 0
            for i in range(len(self.coordinates)):
                dp += (self.coordinates[i] * v1.coordinates[i])

            return dp

        return None

    def includedAngle(self, v1, in_degree = False):
        dp = self.dotProducts(v1)

        mag1 = self.magnitude()
        mag2 = v1.magnitude()

        ret = 0

        if mag1 != 0 and mag2 != 0:
            cossita = dp / (mag1 * mag2)
            rad = math.acos(cossita)
            if in_degree:
                degree = rad * 180.0 / math.pi
                ret = degree
            else:
                ret = rad
        else:

            print 'includedAngle err mag = ', mag1, mag2


        return ret

    # 检查两个向量是否平行
    def checkParallel(self, v1):

        if self.isZero() or v1.isZero() :
            return True

        rad = self.includedAngle(v1)

        # 0 , pi
        return  math.fabs(rad) < 0.0001 or  math.fabs(rad - math.pi)  < 0.0001



    # 检查两个向量是否垂直
    def checkOrthogonal(self, v1):

        if self.isZero() or v1.isZero() :
            return True

        rad = self.includedAngle(v1)

        #   pi/2,
        return  math.fabs(rad - math.pi / 2) < 0.0001


    # 是否零向量
    def isZero(self):

        ret = True
        for i in self.coordinates:
            if math.fabs(i) > 0.00000001:
                ret = False
                break

        return ret

    # 投影向量 v" = |v"| * ub = (v * ub) * ub
    def project(self, baseVec):
        ub = baseVec.normalized()

        projMag = self.dotProducts(ub)

        return ub.scalarMultply(projMag)

    # 垂直向量 vo = v - v"
    def ortho(self, baseVec):
        proj = self.project(baseVec)
        return  self.minus(proj)

    # 叉积, 只支持三维坐标
    def crossProducts(self, v1):
        if len(self.coordinates) == 3 and len(v1.coordinates) == 3 :
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = v1.coordinates
            arr = [0] * 3
            arr[0] =   y1 * z2 - y2 * z1
            arr[1] = -(x1 * z2 - x2 * z1)
            arr[2] =   x1 * y2 - x2 * y1

            return  Vector(arr)

        else:

            print ('crossProducts len err')
            return  None

    # 平行四边形面积
    def paralArea(self, v1):
        cp = self.crossProducts(v1)
        if cp:
            return  cp.magnitude()
        else:
            return  0

    # 三角形面积
    def triangleArea(self, v1):
         return  self.paralArea(v1) / 2.0




    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
