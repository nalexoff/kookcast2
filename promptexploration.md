before i start using the API, I'm going to use chatgpt 3.5 to get a general sense of the prompt that will work for me in the future when i automate the sending of this information

Generate a surfing forecast using the Data provided. Your forecast should be in the format of a table, with the columns "day", "swell", and "wind" and the rows corresponding to a day. In addition to the table, provide a single sentence that determines the best time to surf. The best time to surf will be when the seas are 3 feet and above and the wind is N or NW at any speed, or when the wind is 10 knots or less. If no days meet these conditions, conclude in your forecast that the surfing outlook is not good. 

Data:"""
['Synopsis for the Long Island and Connecticut coastal waters', 'Low pressure passes to our south tonight. High pressure then builds in on Tuesday and remains in control on Wednesday. High pressure gradually moves offshore on Wednesday and then gives way to an approaching cold front Wednesday night. The cold front moves out into the Atlantic Thursday. High pressure returns to the waters Thursday and moves offshore early Friday. A strong frontal system approaches going into the first half of the weekend.']

['TONIGHT   E winds 10 to 15 kt, becoming NE 15 to 20 kt late this evening and early morning, then diminishing to 10 to 15 kt late. Seas 2 to 4 ft. Rain. Vsby 1 to 3 nm after midnight.', 'TUE   N winds 10 to 15 kt with gusts up to 20 kt, diminishing to 5 to 10 kt in the afternoon. Seas 3 to 4 ft. Areas of drizzle. Chance of rain in the morning, then chance of showers in the afternoon. Vsby 1 to 3 nm in the morning.', 'TUE NIGHT   NW winds 5 to 10 kt, becoming N after midnight. Seas around 3 ft. Chance of showers or areas of drizzle in the evening, then slight chance of rain after midnight.', 'WED   N winds around 10 kt with gusts up to 20 kt, becoming W in the afternoon. Seas 2 to 3 ft.', 'WED NIGHT   SW winds 15 to 20 kt with gusts up to 25 kt. Seas 2 to 3 ft, building to 3 to 5 ft after midnight. Slight chance of showers after midnight.', 'THU   NW winds 20 to 25 kt, diminishing to 15 to 20 kt in the afternoon. Seas 3 to 5 ft.', 'THU NIGHT   NW winds 15 to 20 kt, diminishing to 5 to 10 kt after midnight. Seas 2 to 4 ft.', 'FRI   S winds 15 to 20 kt with gusts up to 25 kt. Seas 2 to 3 ft. Chance of showers.', 'FRI NIGHT   SW winds 20 to 25 kt with gusts up to 35 kt. Seas 5 to 8 ft. Showers.', 'SAT   SW winds 25 to 30 kt with gusts up to 40 kt. Seas 9 to 12 ft. Showers likely.', 'SAT NIGHT   W winds 20 to 25 kt with gusts up to 40 kt. Seas 9 to 11 ft. Chance of showers.']
"""





Parse this list: 

['TODAY   W winds 15 to 20 kt with gusts up to 25 kt. Seas 5 to 7 ft. Patchy fog early this morning with vsby locally less than 1 nm.', 'TONIGHT   W winds 15 to 20 kt with gusts up to 25 kt, becoming NW 5 to 10 kt after midnight. Seas 5 to 7 ft, subsiding to 3 to 5 ft after midnight.', 'MON   N winds around 5 kt, becoming E 10 to 15 kt with gusts up to 20 kt in the afternoon. Seas 2 to 3 ft. Rain likely in the afternoon with vsby locally 1 to 3 nm.', 'MON NIGHT   NE winds 15 to 20 kt, becoming N 10 to 15 kt after midnight. Seas 3 to 5 ft. Rain in the evening, then chance of showers after midnight. Vsby locally 1 to 3 nm in the evening.', 'TUE   N winds 10 to 15 kt with gusts up to 20 kt, becoming NW 5 to 10 kt in the afternoon. Seas 3 to 4 ft.', 'TUE NIGHT   NW winds around 10 kt. Seas 2 to 3 ft.', 'WED   NW winds around 10 kt. Seas around 2 ft.', 'WED NIGHT   SW winds 10 to 15 kt with gusts up to 25 kt. Seas 2 to 4 ft.', 'THU   NW winds 15 to 20 kt with gusts up to 25 kt. Seas 3 to 4 ft.', 'THU NIGHT   NW winds 10 to 15 kt with gusts up to 20 kt. Seas 2 to 3 ft.']

Create a table with time, wind, and sea information as the columns. Only create rows in the table when any one of the following conditions is met by the items in the list:

Condition 1: the wind speed (measured in knots or "kt") is less than, around, or equal to 10 knots.

Condition 2: the wind direction (measured in cardinal directions such as "SW" for "Southwest") is North or Northwest



Selenium

Write a Python application that uses Selenium to automate browser actions in Google Chrome. The application should do the following:

Open the Google Chrome browser
Navigate to https://surfcaptain.com/forecast/southampton-new-york
Interact with this button: <div class="summary-day-expand"><i></i></div>
Keep the browser window open on my desktop for 10 seconds after completing the above steps