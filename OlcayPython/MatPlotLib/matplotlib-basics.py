import matplotlib.pyplot as plt
import numpy as np

""""
x = [1,2,3,4]
y = [1,4,9,16]

# plt.plot(x,y,color = "purple",linewidth="5")  # rengi ve çizgi kalınlığı da ayarlanır
plt.plot(x,y,"o--r") # çizgili grafik ve noktaları işaretlenmiş kırmızı renkli (daha fazla ayar için matplotlib sitesi!)
plt.axis([0,6,0,20]) #çizgimizi yukarıdaki bilgilere göre çizer fakat eksenlerimizin sayısal değerlerini burada verdiğimiz gibi yapar

plt.title("Grafik Başlığı")     
plt.xlabel("x label")
plt.ylabel("y label")
"""
"""
x = np.linspace(0,2,100)
plt.plot(x,x,label = "linear",color ="red")
plt.plot(x,x**2,label = "quadratic",color="yellow")
plt.plot(x,x**3,label = "cubic", color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Simple Plot")
plt.legend()

plt.show()
"""
"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2) #2 tane axis alanı oluşturuyoruz. Alt alta 2 tane grafik oldu

axs[0].plot(x,x, color ="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2, color ="green")
axs[1].set_title("quadratic")

plt.tight_layout() #başlıklar iç içe girmesin diye
"""

"""
# aynı grafik içine farklı grafikler
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("grafik başlığı")

axs[0,0].plot(x,x, color ="red")
axs[0,1].plot(x,x**2, color ="blue")
axs[1,0].plot(x,x**3, color ="green")
axs[1,1].plot(x,x**4, color ="purple")
"""
import pandas as pd

df = pd.read_csv("Players.csv")

df = df.drop(["Number"],axis = 1).groupby("Team").mean()
df.plot(subplots=True)
plt.legend()

plt.show()