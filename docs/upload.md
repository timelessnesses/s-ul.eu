# Upload
Initialize class
```py
import suleu
a = suleu.Upload(token)
```
### file upload
```py
a.file_upload(file_path,raw)
```
raw is boolean to choose do you want json res or not  
error will raise if file not found  
warn will raise if file is exceeded 209.714177 megabytes because there's chance s-ul.eu can decline  
### clipboard upload
