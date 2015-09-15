                                                                                       Quality Life
                                                                                       By Tom Biju
                In this program I attempt to solve the data challenge of finding a correlation between the availability of healthcare resources, nutritious food, access to educational opportunities, economic hardship, and life expectancy. Healthcare resources affect life expectancy because people can deal with diseases and other afflictions better. Nutritious food keeps peoples' body in a healthy state. Educational opportunities make people make more informed choices and take less risky actions/engage in less risky behaviors. Economic hardship affects a person's ability to invest in the resources above and many more, including safe, warm shelter, which could be analyzed with other factors to produce more accurate results.

                To analyze this, I downloaded a couple of data files from the Chicago Data Portal. One contained information on the locations of senior centers; this pertained to the availability of healthcare resources. The next one contained data on locations of Farmer's Markets; this pertained to the  availability of healthy food to eat. I also downloaded a file on library locations; this pertains to educational opportunities. I downloaded a file on economic data to find the hardship indices for different neighborhoods. Finally, I downloaded a file for the life expectancies of different neighborhoods.

                The program parsed the data and wrote the life expectancies to csv files as well as hardship data for various neighborhoods. I then created bar charts for these data files using excel and was able to establish a conclusion for the correlation between  economic hardship and life expectancy. Neighborhoods that have higher hardship indices tend to also have lower life expectancies; neighborhoods with lower hardship indices had higher life expectancies.(This was not always the case, but on average it was.) The leads me to conclude their is an inverse relationship between life expectancy and economic hardship index.

                I also found having access to the different resources to support higher life expectancies. For the exceptions, the neighborhoods that have lower life expectancies but possess senior centers, libraries, and farmer's markets, I hypothesized that these areas probably recently gained these resources in order to improve the over quality of life, and in turn, the life expectancy.The cities that I found to possess the resources were printed to the console and ones that possessed all of the resources were written to a file.

                In terms of data structures, I chose to use lists and dictionaries. Lists were good for simple storage and access, but if I wanted to store something as an associative key value pair, I used a dictionary.

                I performed unit tests to test some functionality, and all were successful.

                To conclude, having the resources above, as well as maintaining a low hardship index, seemed to correlate with a higher life expectancy.