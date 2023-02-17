import numpy as np
#let Bending Moment = M and Shear Force = V
#from the question,
L=12
w=10


# Question a.   
#when x=0,
x=0
M=(w*(-6*x**2+6*L*x-L**2))/12 # since L squared would give a positive value, I neglected the (-) sign.
V=w*(L/2-x)


print('ai. When the distance is x=0,Bending moment='+ str(M) +'kNm'+' and shear force='+ str(V)+'kN')
#when x=L,
x=12
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
print('aii. When the distance is x=L, bending moment='+str(M)+'kNm'+' and shear force='+str(V)+'kN')


#Question b
#Simplifying M=0,let M=e for question b.

print('b. The expression for M=0 is given as, 0=x**2-L*x+L**2/6 ')
#The roots for the equation is derived using completion of squares.
#let a=g, b=h, c=i
g=1
h=-L  
i=L**2/6
j=h**2-4*g*i
rootb1=(-h+np.sqrt(j))/2*g
rootb2=(-h-np.sqrt(j))/2*g
print('And the roots are x='+str(rootb1)+'m'+' and x='+str(rootb2)+'m')


#Question c
# To find find the the distance at which V=0,
#let x=k. Simplifying V=0,
k=L/2
print('c. From V = w*(L/2-x)'+',x=L/2'+'. which is, x='+str(k)+'m' )
 

#Question d
#starting from 0 the increasing step is 10mm=0.01m. So,
#and letthe rage of x values be x=n
n =np.arange(0,12.01,0.01)#since we want a step at every 0.01m, there would be 1200 divisions in all.
print('d. The values at a step of 0.01 each is' + str(n)+'m')
M=(w*(-6*n**2+6*L*n-L**2))/12 
print('Using the in the initial variable,Bending Moment at each step is given as '+ str(M)+'kNm')


#Question e
#let the range of x values be x=q
q =np.arange(0,12.01,0.01)#since we want a step at every 0.01m, there would be 1200 divisions in all.
V=w*(L/2-q)
print('e. Using the in the initial variable,Bending Moment at each step is given as '+ str(V)+'kN')


#Question f
#let r be the absolute values of the array of M.
r=abs(M)
s=min(r)
print('f. The minimum value of the bending moment is '+str(s)+'kN')
#Equating the bending moment equation to the min value, M=s.
#The minimum value, the equation is x**2 - Lx + (L**2/6)+(2*s)/w = 0. Where x is the point at which bending moment is minimum.
#Solving the equation using completion of squares, a=t, b=u c=y
t=1
u=-12
y=(L**2/6)+(2*s)/w
z=u**2-4*t*y
rootf1=(-u+np.sqrt(z))/2*t
rootf2=(-u-np.sqrt(z))/2*t
print('The points at which bending moments is minimum is x='+str(rootf1)+'m'+' and x='+str(rootf2)+'m')


#Question g
#let the relative error in the points be error1 and error2
#let the relative error be in percentages
error1=(((rootb1-rootf1)/rootb1)*100)
error2=(((rootf2-rootb2)/rootf2)*100)
print('g. The relative errors between the points of contra-flexure are '+str(error1)+'%'+' and '+str(error2)+'%')


#Question h
#let the maximum value be maxofM and minimum value be minofM
maxofM=max(M)
minofM=min(M)
# for maximum value, the equation is x**2 - Lx + (L**2/6)+(2*maxofM)/w = 0

a=1
b=-L
c=(L**2/6)+(2*maxofM)/w
h=b**2-4*a*c
rooth1=(-b+np.sqrt(h))/2*a
rooth2=(-b-np.sqrt(h))/2*a
print('hi. The points at which maximum bending moment occurs is at x='+str(rooth1)+'m'+' and x='+str(rooth2)+'m')

# for minimum value, the equation is x**2 - Lx + (L**2/6)+(2*minofM)/w = 0
a=1
b=-L
c=(L**2/6)+(2*minofM)/w
hh=b**2-4*a*c
root_h1=(-b+np.sqrt(hh))/2*a
root_h2=(-b-np.sqrt(hh))/2*a
print('hii. The points at which minimum bending moment occurs is at x='+str(root_h1)+'m'+' and x='+str(root_h2)+'m')

https://github.com/Henryadj3

