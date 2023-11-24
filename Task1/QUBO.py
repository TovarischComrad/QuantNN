import numpy as np
import pickle


def fQ1():
  Q1 = np.zeros((890,890))
  for i in range(24):
    Q1[2+6*i][2+6*i] += 1
    Q1[144 + 6*i][144 + 6*i] += 1
    Q1[288 + 5+6][288 + 5+6] += 1
    Q1[432+1+6*i][432+1+6*i] +=1
    Q1[576 +1 +6*1][576 +1 +6*1] += 1
  return Q1


def fQ2():
  Q2 = np.zeros((890,890))
  for k in range(10):
    for i in range(72):
      Q2[i+72*k][i+72*k] += -7
      for j in range(72):
        if i != j :
          Q2[i+72*k][j+72*k] +=1
  return Q2


def fQ3():
  Q3 = np.zeros((890,890))
  for k in range(120):
    Q3[720+k][720+k] += - 3
    for i in range(6*k,6*k+6):
      Q3[i][i] += -3
      Q3[720 + k][i] += 1
      Q3[i][720+k] += 1
      for j in range(6*k,6*k+6):
        if i != j :
          Q3[i][j] += 1
  return Q3


def fQ4():
  Q4 = np.zeros((890,890))
  for k in range(5):
    for i in range(144*k,144*k + 36):
      Q4[i][i] += -39
      Q4[i+72][i+72] += -39
      for l in range(144*k,144*k+36):
        Q4[l+72][i] += 1
        Q4[i][l+72] +=1
        if l != i :
          Q4[l][i] += 1
          Q4[i+72][l+72] +=1
      for j in range(5):
        Q4[i][840+ j + 5*k] += 1
        Q4[840+ j + 5*k][i] += 1
        Q4[i +72][840 + j +5*k] += 1
        Q4[840 + j +5*k][i +72] += 1
    for j in range(5):
      Q4[840 + j + 5*k][840+j+5*k] += -39 * 2**j
      for j2 in range(5):
        if j !=j2 :
          Q4[840+j2 + 5*k][840+j + 5*k] += 2**(j+j2)
  return Q4


def fQ5():
  Q5 = np.zeros((890,890))
  for k in range(5):
    for i in range(144*k,144*k + 36):
      Q5[i][i] += -39
      Q5[i+72][i+72] += -39
      for l in range(144*k,144*k+36):
        Q5[i][l+72] += 1
        Q5[l+72][i] += 1
        if l != i :
          Q5[l][i] += 1
          Q5[l+72][i+72] +=1
      for j in range(5):
        Q5[i][840+25+ j + 5*k] += 1
        Q5[840+25+ j + 5*k][i] += 1
        Q5[i +72][840+25 + j +5*k] += 1
        Q5[840+25 + j +5*k][i +72] += 1
    for j in range(5):
      Q5[840 +25+ j + 5*k][840+25+j+5*k] += -39 * 2**j
      for j2 in range(5):
        if j !=j2 :
          Q5[840+25+j2 + 5*k][840+25+j + 5*k] += 2**(j+j2)
  return Q5


def fQ6():
    Q6 = np.zeros((890,890))
    for i in range(72):
        for k in range(10):
            for l in range(10):
                if k != l:
                    Q6[k * 72 + i][l * 72 + i] +=  1
    return Q6


def result(P1,P2,P3,P4,P5,P6):
  Q = np.zeros((890,890))
  Q = P1 * fQ1() + P2 * fQ2() + P3 * fQ3() + P4 * fQ4() + P5 * fQ5() + P6 * fQ6()
  return Q


P1 = 100
P2 = 50
P3 = 50
P4 = 5
P5 = 5
P6 = 150
Q = result(P1,P2,P3,P4,P5,P6)


with open('quantnn.pkl', 'wb') as file:
  pickle.dump(Q, file)
