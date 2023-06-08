import numpy as np
import streamlit as slt
import pickle as pkl

model=pkl.load(open('Laptop_MLmodel.pkl','rb'))
#df=pkl.load(open('final_df','rb'))

slt.header('Laptop Price Predictor')



company = slt.selectbox('Select the Brand',['Apple', 'Asus', 'Chuwi',
       'Dell', 'Fujitsu', 'Google', 'HP',
       'Huawei', 'LG', 'Lenovo', 'MSI',
       'Mediacom', 'Microsoft', 'Razer',
       'Samsung', 'Toshiba', 'Vero', 'Xiaomi'])

if company == 'Apple':
       Company_Apple = 1
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Asus' :
       Company_Apple = 0
       Company_Asus  = 1
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Chuwi':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 1
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Dell':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 1
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Fujitsu':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 1
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Google':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 1
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'HP':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 1
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Huawei':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 1
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'LG':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 1
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Lenovo':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 1
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'MSI':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 1
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Mediacom':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 1
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company =='Microsoft':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 1
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Razer':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 1
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Samsung':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 1
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Toshiba':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 1
       Company_Vero	= 0
       Company_Xiaomi = 0

elif company == 'Vero':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 1
       Company_Xiaomi = 0

elif company == 'Xiaomi':
       Company_Apple = 0
       Company_Asus  = 0
       Company_Chuwi = 0
       Company_Dell  = 0
       Company_Fujitsu = 0
       Company_Google = 0
       Company_HP	= 0
       Company_Huawei = 0
       Company_LG	= 0
       Company_Lenovo = 0
       Company_MSI	= 0
       Company_Mediacom = 0
       Company_Microsoft	= 0
       Company_Razer	= 0
       Company_Samsung	= 0
       Company_Toshiba	= 0
       Company_Vero	= 0
       Company_Xiaomi = 1


type = slt.selectbox('Select the Type of Laptop',['Gaming', 'Notebook', 'Ultrabook',
       'Workstation'])

TypeName_Gaming	= 0
TypeName_Notebook = 0
TypeName_Ultrabook	= 0
TypeName_Workstation = 0

if type == 'Gaming':
       TypeName_Gaming = 1
elif type == 'Notebook':
       TypeName_Notebook = 1
elif type == 'Ultrabook':
       TypeName_Ultrabook = 1
elif type == 'Workstation':
       TypeName_Workstation = 1


processor = slt.selectbox('Select the Processor',['Intel Core i3', 'Intel Core i5',
       'Intel Core i7', 'Intel Other Processor',])

Core_i3 = 0
Core_i5 = 0
Core_i7 = 0
Other_Processor = 0

if processor == 'Intel Core i3':
       Core_i3 = 1
elif processor == ' Intel Core i5':
       Core_i5 = 1
elif processor == 'Intel Core i7':
       Core_i7 = 1
elif processor == 'Cpu_Intel Other Processor':
       Other_Processor = 1


os = slt.selectbox ('Choose the Operating System',['Other OS',
       'Window OS'])

Other_OS = 0
Window_OS = 0

if os == 'Other OS':
       Other_OS = 1
elif os == 'Window OS':
       Window_OS = 1


gpu = slt.selectbox('Choose the GPU Brand',['Intel', 'Nvidia'])
Gpu_Brand_Intel = 0
Gpu_Brand_Nvidia = 0

if gpu == 'Intel':
       Gpu_Brand_Intel =1
elif gpu == "Nvidia":
       Gpu_Brand_Nvidia =1



size = slt.selectbox ('Size of Laptop in Inches',['15.6','14.0','13.3','17.3','12.5','11.6','12.0','13.5','13.9',
                                        '10.1','15.4','12.3','15.0','13.0','18.4','17.0','14.1','11.3'])
size = float(size)

ram=slt.selectbox('RAM in GB',['2','4', '6', '8', '12', '16', '24', '32', '64'])
ram = int(ram)

touchscreen = slt.selectbox('Touchscreen',['Yes','No'])
if touchscreen == 'Yes':
       touchscreen = 1
elif touchscreen == 'No':
       touchscreen = 0

ips = slt.selectbox('IPS Panel',['Yes','No'])
if ips == 'Yes':
       ips = 1
elif ips == 'No':
       ips = 0


y_res = slt.selectbox('Screen Resolution in Pixels',['1080','768','2160','1800','1440','900','1600','1504','1200','1824'])
y_res = int(y_res)

ssd = slt.selectbox('SSD in GB',['256','0','128','512','1000', '32','180','16','64','240','8' ])
ssd = int(ssd)

hdd = slt.selectbox('HDD in GB ',['0','32','128','500','1000','2000'])
hdd = int(hdd)

weight = slt.slider('Enter Weight in Kgs',min_value=0.69,max_value= 4.7)

user_data = [size,ram,weight,touchscreen,ips,y_res,ssd,hdd,Company_Apple, Company_Asus, Company_Chuwi,
             Company_Dell,Company_Fujitsu, Company_Google, Company_HP, Company_Huawei,Company_LG,
             Company_Lenovo, Company_MSI, Company_Mediacom,
             Company_Microsoft, Company_Razer, Company_Samsung,
             Company_Toshiba, Company_Vero, Company_Xiaomi,
             TypeName_Gaming,TypeName_Notebook,TypeName_Ultrabook,TypeName_Workstation,
             Core_i3,Core_i5,Core_i7,Other_Processor,
             Other_OS,Window_OS,Gpu_Brand_Intel, Gpu_Brand_Nvidia]



if slt.button('Show Laptop Price'):
       pred = model.predict(np.array(user_data).reshape(1, -1))
       pred = np.exp(pred)
       slt.text('Laptop Price in Rs:')
       slt.text(pred[0].round(0))
