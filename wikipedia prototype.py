# importing the module 
import wikipedia 
  
# setting language to hindi 
wikipedia.set_lang("en") 
  
# printing the summary 
print(wikipedia.summary(input("enter what to search:")))
