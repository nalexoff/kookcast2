before i start using the API, I'm going to use chatgpt 3.5 to get a general sense of the prompt that will work for me in the future when i automate the sending of this information

Parse this list: 

['TODAY   W winds 15 to 20 kt with gusts up to 25 kt. Seas 5 to 7 ft. Patchy fog early this morning with vsby locally less than 1 nm.', 'TONIGHT   W winds 15 to 20 kt with gusts up to 25 kt, becoming NW 5 to 10 kt after midnight. Seas 5 to 7 ft, subsiding to 3 to 5 ft after midnight.', 'MON   N winds around 5 kt, becoming E 10 to 15 kt with gusts up to 20 kt in the afternoon. Seas 2 to 3 ft. Rain likely in the afternoon with vsby locally 1 to 3 nm.', 'MON NIGHT   NE winds 15 to 20 kt, becoming N 10 to 15 kt after midnight. Seas 3 to 5 ft. Rain in the evening, then chance of showers after midnight. Vsby locally 1 to 3 nm in the evening.', 'TUE   N winds 10 to 15 kt with gusts up to 20 kt, becoming NW 5 to 10 kt in the afternoon. Seas 3 to 4 ft.', 'TUE NIGHT   NW winds around 10 kt. Seas 2 to 3 ft.', 'WED   NW winds around 10 kt. Seas around 2 ft.', 'WED NIGHT   SW winds 10 to 15 kt with gusts up to 25 kt. Seas 2 to 4 ft.', 'THU   NW winds 15 to 20 kt with gusts up to 25 kt. Seas 3 to 4 ft.', 'THU NIGHT   NW winds 10 to 15 kt with gusts up to 20 kt. Seas 2 to 3 ft.']

Create a table with time, wind, and sea information as the columns. Only create rows in the table when any one of the following conditions is met by the items in the list:

Condition 1: the wind speed (measured in knots or "kt") is less than, around, or equal to 10 knots.

Condition 2: the wind direction (measured in cardinal directions such as "SW" for "Southwest") is North or Northwest