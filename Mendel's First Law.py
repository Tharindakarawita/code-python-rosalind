def Mendel(k,m,n):
    p = k + m + n
    x = (k - 1) + m + n
    y = k + (m - 1) + n
    z = k + m + (n - 1)
    Ratio_dominant1 = ((k*(k-1))+(m*k)+(n*k))/(x*p)
    Ratio_dominant2 = ((k*m)+(3*m*(m-1)/4)+((n*m))/2)/(y*p)
    Ratio_dominant3 = ((k*n)+((m*n)/2))/(z*p)
    Ratio_dominant = Ratio_dominant1 + Ratio_dominant2 + Ratio_dominant3
    return print(round(Ratio_dominant,5))

Mendel(24,28,26)


