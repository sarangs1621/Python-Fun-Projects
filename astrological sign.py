def zodiac_sign(day, month): 
      
    # checks month and date within the valid range 
    # of a specified zodiac 
    if month == 'december' or 'dec': 
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
          
    elif month == 'january' or 'jan': 
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
          
    elif month == 'february' or 'feb': 
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
          
    elif month == 'march': 
        astro_sign = 'Pisces' if (day < 21) else 'aries'
          
    elif month == 'april': 
        astro_sign = 'Aries' if (day < 20) else 'taurus'
          
    elif month == 'may': 
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
          
    elif month == 'june': 
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
          
    elif month == 'july': 
        astro_sign = 'Cancer' if (day < 23) else 'leo'
          
    elif month == 'august' or 'aug': 
        astro_sign = 'Leo' if (day < 23) else 'virgo'
          
    elif month == 'september' or'sept': 
        astro_sign = 'Virgo' if (day < 23) else 'libra'
          
    elif month == 'october' or 'oct': 
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
          
    elif month == 'november' or 'nov': 
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
          
    print("your astrological sign is:",astro_sign) 
      
# Driver code  
if __name__ == '__main__': 
    day = int(input('enter the date:'))
    month = input("enter the monthe:")
    zodiac_sign(day, month) 
