# **Web Scrapper**

Repository to scrape a website

### **Dependencies**
```
Python >= 3.8
Sqlite
```

### **Virtual Environment Setup**
>Open command prompt and cd to Desktop
```
$ cd PATH_TO_DESKTOP
```

>Install Virtualenv
```
$ pip install virtualenv==20.0.23
```

>Create a Virtualenv
```
$ virtualenv -p python3.8 venv
```

>Activate Virtualenv
```
$ source venv/bin/activate
```

### **Repository Setup**
>Clone Repository
```
$ git clone https://github.com/itsayushbansal/scrapper.git
```
>Navigate to the Repository
```
$ cd scrapper
```

### **Requirements Setup**
>Install requirements
```
$ pip install -r requirements.txt
```

### **Environment variables Setup**
>Create a **.env** file(inside scrapper dir) with these variables:
```
export USERNAME={{ PEPCO SIGNIN USERNAME }}
export PASSWORD={{ PEPCO SIGNIN PASSWORD }}
```

>Set Environment variables:
```
export USERNAME={{ PEPCO SIGNIN USERNAME }}
export PASSWORD={{ PEPCO SIGNIN PASSWORD }}
```

### **Sqlite Setup**
>Install Sqlite:
```
$ sudo apt install sqlite3
```

### **Run the Application**
```
$ python3 scrape_web/main.py
```
