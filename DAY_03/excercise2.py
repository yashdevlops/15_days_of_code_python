import time 
def get_greeting():
    current_hour = time.localtime().tm_hour
    if 4<= current_hour <12:
        greeting="Good Morning....."
    elif 12<= current_hour < 17:
        greeting="Good Afternoon...."
    elif 17<= current_hour <21:
        greeting = "Good Evening...."        
    else:
        greeting = "Good Night......."  
    return greeting    
def main():
    greeting=get_greeting()
    current_time=time.strftime('%H:%M:%S')
    print(f"{greeting}! 🌟")
    print(f"Current time: {current_time}")
if __name__ == "__main__":
    main()    