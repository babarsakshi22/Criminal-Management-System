from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class CriminalManagement:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')
        
        lbl_title=Label(self.root,text="CRIMINAL MANAGEMENT SYSTEM",font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70 )
        
      # Variables
      
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()
       
        # Main Logo of Criminal Management System
        
        img_logo=Image.open("Images/Logo.jpg")
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=240,y=5,width=60,height=60)
        
        # Image frame 
        
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='grey')
        img_frame.place(x=0,y=70,width=1530,height=130)
        
        # 1st Image
        
        img1=Image.open("Images/PoliceGun.jpg")
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        
        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)
        
        
        # 2nd Image
        
        img2=Image.open("Images/PoliceArrest.jpg")
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)
        
        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)
        
        # 3rd Image
       
        img3=Image.open("Images/Arrest.jpg")
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)
        
        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=530,height=160)
        
        # Main Information Frame
        
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='Purple')
        Main_frame.place(x=13,y=205,width=1500,height=580)
        
        # Upper Frame
        
        Upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal Information",font=('times new roman',20,'bold'),fg='red',bg='White')
        Upper_frame.place(x=10,y=10,width=1480,height=270)
         
         #Labels Entry
         
         # Case ID
         
        caseid=Label(Upper_frame,text='Case ID:',font=('arial',11,'bold'),bg='White')      
        caseid.grid(row=0,column=0,padx=2,sticky=W)
        
        caseentry=ttk.Entry(Upper_frame,width=22,textvariable=self.var_case_id,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)
        
        # Criminal No
        
        lbl_Criminal_no=Label(Upper_frame,text='Criminal No:',font=('arial',11,'bold'),bg='White')      
        lbl_Criminal_no.grid(row=0,column=2,padx=2,sticky=W,pady=7)
        
        txt_Criminal_no=ttk.Entry(Upper_frame,width=22,textvariable=self.var_criminal_no,font=('arial',11,'bold'))
        txt_Criminal_no.grid(row=0,column=3,padx=2,pady=7)
        
        # Criminal Name
        
        lbl_Name=Label(Upper_frame,text='Criminal Name:',font=('arial',11,'bold'),bg='White')      
        lbl_Name.grid(row=1,column=0,padx=2,sticky=W,pady=7)
        
        txt_Name=ttk.Entry(Upper_frame,width=22,textvariable=self.var_name,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,sticky=W,padx=2,pady=7)
        
        
         # NickName of the Criminal 
        
        lbl_NickName=Label(Upper_frame,text='NickName:',font=('arial',11,'bold'),bg='White')      
        lbl_NickName.grid(row=1,column=2,padx=2,sticky=W,pady=7)
        
        txt_NickName=ttk.Entry(Upper_frame,width=22,textvariable=self.var_nickname,font=('arial',11,'bold'))
        txt_NickName.grid(row=1,column=3,padx=2,pady=7)
        
         # Arrest Date of the Criminal
        
        lbl_ArrestDate=Label(Upper_frame,text='Arrest Date:',font=('arial',11,'bold'),bg='White')      
        lbl_ArrestDate.grid(row=2,column=0,padx=2,sticky=W,pady=7)
        
        txt_ArrestDate=ttk.Entry(Upper_frame,width=22,textvariable=self.var_arrest_date,font=('arial',11,'bold'))
        txt_ArrestDate.grid(row=2,column=1,padx=2,pady=7)
        
         # Date of Crime
        
        lbl_CrimeDate=Label(Upper_frame,text='Date of Crime:',font=('arial',11,'bold'),bg='White')      
        lbl_CrimeDate.grid(row=2,column=2,padx=2,sticky=W,pady=7)
        
        txt_CrimeDate=ttk.Entry(Upper_frame,width=22,textvariable=self.var_date_of_crime,font=('arial',11,'bold'))
        txt_CrimeDate.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
           
         # Address of the Criminal
        
        lbl_Address=Label(Upper_frame,text='Address:',font=('arial',11,'bold'),bg='White')      
        lbl_Address.grid(row=3,column=0,padx=2,sticky=W,pady=7)
        
        txt_Address=ttk.Entry(Upper_frame,width=22,textvariable=self.var_address,font=('arial',11,'bold'))
        txt_Address.grid(row=3,column=1,sticky=W,padx=2,pady=7)
        
        
        # Age of the Criminal
        
        lbl_Age=Label(Upper_frame,text='Age of Criminal:',font=('arial',11,'bold'),bg='White')      
        lbl_Age.grid(row=3,column=2,padx=2,sticky=W,pady=7)
        
        txt_Age=ttk.Entry(Upper_frame,width=22,textvariable=self.var_age,font=('arial',11,'bold'))
        txt_Age.grid(row=3,column=3,padx=2,pady=7)
        
           
         # Occupution of the Criminal
        
        lbl_Occupation=Label(Upper_frame,text='Occupation:',font=('arial',11,'bold'),bg='White')      
        lbl_Occupation.grid(row=4,column=0,padx=2,sticky=W,pady=7)
        
        txt_Occupation=ttk.Entry(Upper_frame,width=22,textvariable=self.var_occupation,font=('arial',11,'bold'))
        txt_Occupation.grid(row=4,column=1,padx=2,pady=7)
           
        
          # Birthmark of the Criminal
        
        lbl_Birthmark=Label(Upper_frame,text='Birth Mark:',font=('arial',11,'bold'),bg='White')      
        lbl_Birthmark.grid(row=4,column=2,padx=2,sticky=W,pady=7)
        
        txt_Birthmark=ttk.Entry(Upper_frame,width=22,textvariable=self.var_birthmark,font=('arial',11,'bold'))
        txt_Birthmark.grid(row=4,column=3,sticky=W,padx=2,pady=7)
         
        
         # Crime Type
        
        lbl_CrimeType=Label(Upper_frame,text='Crime Type:',font=('arial',11,'bold'),bg='White')      
        lbl_CrimeType.grid(row=0,column=4,padx=2,sticky=W,pady=7)
        
        txt_CrimeType=ttk.Entry(Upper_frame,width=22,textvariable=self.var_crime_type,font=('arial',11,'bold'))
        txt_CrimeType.grid(row=0,column=5,padx=2,pady=7)
              
        
         # Father Name
        
        lbl_FatherName=Label(Upper_frame,text='Father Name:',font=('arial',11,'bold'),bg='White')      
        lbl_FatherName.grid(row=1,column=4,padx=2,sticky=W,pady=7)
        
        txt_FatherName=ttk.Entry(Upper_frame,width=22,textvariable=self.var_father_name,font=('arial',11,'bold'))
        txt_FatherName.grid(row=1,column=5,padx=2,pady=7)
        
         # Gender
        
        lbl_Gender=Label(Upper_frame,text='Gender:',font=('arial',11,'bold'),bg='White')      
        lbl_Gender.grid(row=2,column=4,padx=2,sticky=W,pady=7)
        
         #Wanted
         
        lbl_Wanted=Label(Upper_frame,text='Most Wanted:',font=('arial',11,'bold'),bg='White')      
        lbl_Wanted.grid(row=3,column=4,padx=2,sticky=W,pady=7)
         
        #Radio Button for gender
        radio_frame_gender=Frame(Upper_frame,bd=2,relief=RIDGE,bg='White')
        radio_frame_gender.place(x=715,y=90,width=190,height=30)   
        
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='White')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
         
        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='White')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        
        
        #Radio Button for Wanted
        radio_frame_wanted=Frame(Upper_frame,bd=2,relief=RIDGE,bg='White')
        radio_frame_wanted.place(x=715,y=130,width=190,height=30)   
       
        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='White')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
         
        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='White') 
        no.grid(row=0,column=2,pady=2,padx=5,sticky=W)
        
        # Buttons
        
        Button_frame=Frame(Upper_frame,bd=2,relief=RIDGE,bg='White')
        Button_frame.place(x=5,y=196,width=490,height=30)   
        
        # Add Button 
        
        btn_add=Button(Button_frame,command=self.add_data,text='Record Save',font=('arial',9,'bold'),width=15,bg='Blue',fg='White')
        btn_add.grid(row=0,column=0,padx=3,pady=2)
         
        # Update Button 
        
        btn_Update=Button(Button_frame,command=self.update_data,text='Update',font=('arial',9,'bold'),width=15,bg='Blue',fg='White')
        btn_Update.grid(row=0,column=2,padx=3,pady=2)
         
         # Delete Button
         
        btn_delete=Button(Button_frame,command=self.delete_data,text='Delete',font=('arial',9,'bold'),width=15,bg='Blue',fg='White')
        btn_delete.grid(row=0,column=3,padx=3,pady=2)
         
       # Clear Button
         
        btn_clear=Button(Button_frame,command=self.clear_data,text='Clear',font=('arial',9,'bold'),width=15,bg='Blue',fg='White')
        btn_clear.grid(row=0,column=4,padx=3,pady=2)
        
        # Background Right Side Image
        
        img_crime=Image.open("Images/Background.jpg")
        img_crime=img_crime.resize((450,245),Image.ANTIALIAS)
        self.photocrime=ImageTk.PhotoImage(img_crime)
        
        self.img_crime=Label(Upper_frame,image=self.photocrime)
        self.img_crime.place(x=950,y=0,width=500,height=220)
           
        # Down Frame
        
        Down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal Information Table",font=('times new roman',20,'bold'),fg='red',bg='White')
        Down_frame.place(x=10,y=280,width=1480,height=270)
         
         
        Search_frame=LabelFrame(Down_frame,bd=2,relief=RIDGE,text="Search Criminal Record",font=('times new roman',15,'bold'),fg='red',bg='white')
        Search_frame.place(x=0,y=0,width=1470,height=60)
        
        Search_by=Label(Search_frame,text='Search By:',font=('arial',11,'bold'),bg='red',fg='White')      
        Search_by.grid(row=0,column=0,sticky=W,padx=2)
        
        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=('arial',11,'bold'),width=18,state='readonly')
        combo_search_box['value']=('select option','Case_Id','Criminal_No')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=2)
        
        self.var_search=StringVar()
        Seach_txt=ttk.Entry(Search_frame,textvariable=self.var_search,width=18,font=('arial',11,'bold'))
        Seach_txt.grid(row=0,column=2,sticky=W,padx=3,pady=5) 
        
        # Search Button
         
        btn_Search=Button(Search_frame,command=self.search_data(),text='Search',font=('arial',9,'bold'),width=15,bg='Blue',fg='White')   #command=self.search_data()
        btn_Search.grid(row=0,column=3,padx=3,pady=5)
        
        
       # All Button
         
        btn_all=Button(Search_frame,text='Show All',font=('arial',9,'bold'),width=15,bg='Blue',fg='White')         #command=self.fetch_data()
        btn_all.grid(row=0,column=4,padx=3,pady=5)
        
        
        crimeagency=Label(Search_frame,text='NATIONAL CRIME AGENCY',font=('arial',24,'bold'),fg='green',bg='white')      
        crimeagency.grid(row=0,column=5,padx=160,sticky=W)
        
        
        
        table_frame=Frame(Down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)
        
        #Scroll Bar
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)
        
        
        self.criminal_table.heading('1',text='Case_Id')
        self.criminal_table.heading('2',text='Criminal_No')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NikeName')
        self.criminal_table.heading('5',text='Arrest Date')
        self.criminal_table.heading('6',text='Crime of Date')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupution')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')
        
        self.criminal_table['show']='headings'
        
        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=100)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=100)
        self.criminal_table.column("7",width=100)
        self.criminal_table.column("8",width=100)
        self.criminal_table.column("9",width=100)
        self.criminal_table.column("10",width=100)
        self.criminal_table.column("11",width=100)
        self.criminal_table.column("12",width=100)
        self.criminal_table.column("13",width=100)
        self.criminal_table.column("14",width=100)
        
        self.criminal_table.pack(fill=BOTH,expand=1)
        
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
      
        self.fetch_data()
        
      
        
    #Add Function
    def add_data(self):   
        if self.var_case_id.get()=="":
            messagebox.showwerror('Error','All Fields are required')
        else:
            try:
           
              conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='management')
              my_cursor=conn.cursor()
              my_cursor.execute('insert into criminal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                        
                                                                                                          self.var_case_id.get(),
                                                                                                          self.var_criminal_no.get(),
                                                                                                          self.var_name.get(),
                                                                                                          self.var_nickname.get(),
                                                                                                          self.var_arrest_date.get(),
                                                                                                          self.var_date_of_crime.get(),
                                                                                                          self.var_address.get(),
                                                                                                          self.var_age.get(),
                                                                                                          self.var_occupation.get(),
                                                                                                          self.var_birthmark.get(),
                                                                                                          self.var_crime_type.get(),
                                                                                                          self.var_father_name.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_wanted.get()
                                                                                                          ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo('Success','Criminal Record has been Added')
              
            except Exception as es:
              messagebox.showerror('Error',f'Due to{str(es)}')  
                                 
   #Fetch Data
    
    def fetch_data(self):
      conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='management') 
      my_cursor=conn.cursor()
      my_cursor.execute('select* from criminal1')
      data=my_cursor.fetchall()
      if len(data)!=0:
        self.criminal_table.delete(*self.criminal_table.get_children())
        for i in data:
          self.criminal_table.insert('',END,values=i)
        conn.commit()
      conn.close()
      
    def get_cursor(self,event=""):
      cursor_row=self.criminal_table.focus()
      content=self.criminal_table.item(cursor_row)
      data=content['values']
      
      self.var_case_id.set(data[0])  
      self.var_criminal_no.set(data[1])
      self.var_name.set(data[2])
      self.var_nickname.set(data[3])
      self.var_arrest_date.set(data[4])
      self.var_date_of_crime.set(data[5])
      self.var_address.set(data[6])
      self.var_age.set(data[7])
      self.var_occupation.set(data[8])
      self.var_birthmark.set(data[9])
      self.var_crime_type.set(data[10])
      self.var_father_name.set(data[11])
      self.var_gender.set(data[12])
      self.var_wanted.set(data[13])
     
      
  # Update
  
    def update_data(self):   
      if self.var_case_id.get()=="":
        messagebox.showerror('Error','All fields are required')
      else:
          try:
             update=messagebox.askyesno('Update','Are you sure update this criminal Record')
             if update>0:
               conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='management') 
               my_cursor=conn.cursor()
               my_cursor.execute('update criminal1 set Criminal_No=%s,name=%s,nickname=%s,arrest_date=%s,date_of_crime=%s,address=%s,age=%s,occupation=%s,birthmark=%s,crime_type=%s,father_name=%s,gender=%s,wanted=%s where Case_Id=%s',(
                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             self.var_criminal_no.get(),
                                                                                                                                                                                                                                             self.var_name.get(),
                                                                                                                                                                                                                                             self.var_nickname.get(),
                                                                                                                                                                                                                                             self.var_arrest_date.get(),
                                                                                                                                                                                                                                             self.var_date_of_crime.get(),
                                                                                                                                                                                                                                             self.var_address.get(),
                                                                                                                                                                                                                                             self.var_age.get(),
                                                                                                                                                                                                                                             self.var_occupation.get(),
                                                                                                                                                                                                                                             self.var_birthmark.get(),
                                                                                                                                                                                                                                             self.var_crime_type.get(),
                                                                                                                                                                                                                                             self.var_father_name.get(),
                                                                                                                                                                                                                                             self.var_gender.get(),
                                                                                                                                                                                                                                             self.var_wanted.get(),
                                                                                                                                                                                                                                             self.var_case_id.get(),
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           ))
              
             else:
              if not update:
               return 
             conn.commit()
             self.fetch_data()
             self.clear_data()
             conn.close()
             messagebox.showinfo('Success','Criminal Record successfully Updated')
             
          except Exception as es:
              messagebox.showerror('Error',f'Due to{str(es)}')  
              
              
  # Delete
    
    def delete_data(self): 
      if self.var_case_id.get()=="":
         messagebox.showerror('Error','All fields are required')
      else:
          try:
             delete=messagebox.askyesno('Delete','Are you sure delete this criminal Record')
             if delete>0:
                  conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='management') 
                  my_cursor=conn.cursor()
                  sql='delete from criminal1 where Case_Id=%s'
                  value=(self.var_case_id.get(),)
                  my_cursor.execute(sql,value)
             else:
               if not delete:
                return  
             conn.commit()
             self.fetch_data()
             self.clear_data()
             conn.close()
             messagebox.showinfo('Success','Criminal Record successfully deleted')
             
          except Exception as es:
              messagebox.showerror('Error',f'Due to{str(es)}')   
             
   # Clear 
   
    def clear_data(self):  
      
      self.var_case_id.set("")  
      self.var_criminal_no.set("")
      self.var_name.set("")
      self.var_nickname.set("")
      self.var_arrest_date.set("")
      self.var_date_of_crime.set("")
      self.var_address.set("")
      self.var_age.set("")
      self.var_occupation.set("")
      self.var_birthmark.set("")
      self.var_crime_type.set("")
      self.var_father_name.set("")
      self.var_gender.set("")
      self.var_wanted.set("")
 
 # Search

    def  search_data(self):
      if self.var_com_search.get()=="":
         messagebox.showerror('Error','All fields are required') 
      else:
          try:
              conn=mysql.connector.connect(host='localhost',username='root',password='test@123',database='management') 
              my_cursor=conn.cursor()
              my_cursor.execute('select * from criminal1 where' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"'%"))
              rows=my_cursor.fetchall()
              if len(rows)!=0:
                  self.criminal_table.delete(*self.criminal_table.get_children())
                  for i in rows:
                      self.criminal_table.insert('',END,values=i)
              conn.commit()
              conn.close()
                  
          except Exception as es:
               messagebox.showerror('Error',f'Due to{str(es)}') 
                                           
if __name__=="__main__":
    root=Tk()        
    obj=CriminalManagement(root)
    root.mainloop()