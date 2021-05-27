'''file handling -1.file handing is very important for accessing other data.
                  2.there are three modes in file hanling as read , write and append.
                  3.in read you can red only
                  4.in write you can write a data but when you write new line old one gets deletd
                  5.append adds new data and keeps olds data as it is.
                  6.if you open a file but that file doesnt exist it creates a new file with that name but mode
                  must be append.
                  7. we also can acess image using this
                  ..for eg we are aceesed a demo file below'''
#EG-

f1 = open("abc.txt",'a')
f1.write("encryptt side support encrypted communication, an eavesdropper snooping ...")
f1 = open("abc.txt",'r')
for data in f1:
    print(data)