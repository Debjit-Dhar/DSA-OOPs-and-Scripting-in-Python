from numpy import random
import matplotlib.pyplot as pl
import seaborn as sns
pl.title('RANDOM DISTRIBUTIONS')
sns.distplot(random.normal(size=10), hist=False,label='Normal Distribution')
sns.distplot(random.binomial(n=10,p=0.4,size=10), hist=False,label='Binomial Distribution')
sns.distplot(random.poisson(lam=2,size=10), hist=False,label='Poisson Distribution')
sns.distplot(random.uniform(size=10), hist=False,label='Uniform Distribution')
sns.distplot(random.logistic(loc=1,scale=2,size=10), hist=False,label='Logistic Distribution')
sns.distplot(random.multinomial(n=10,pvals=[0.1,0.1,0.2,0.05,0.05,0.1,0.1,0.1,0.025,0.175],size=10), hist=False,label='Multinomial Distribution')
sns.distplot(random.exponential(size=10), hist=False,label='Exponential Distribution')
sns.distplot(random.chisquare(df=2,size=10), hist=False,label='Chi Square Distribution')
sns.distplot(random.rayleigh(size=10), hist=False,label='Rayleigh Distribution')
sns.distplot(random.pareto(a=2,size=10), hist=False,label='Pareto Distribution')
sns.distplot(random.zipf(a=2,size=10), hist=False,label='Zipf Distribution')
pl.legend()
pl.show()