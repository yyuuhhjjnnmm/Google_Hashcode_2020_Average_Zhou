# Google Hashcode 2020 Average Zhou
Google Hashcode 2020 Qualifier Round  
Team: Average Joe's  
Members: David Zhou, Luka Filipovic, Ted Clancy, Viktor Zhou  
Date: February 20th, 2020  

# Question:  
We are given a list of libraries, each library has the follow:
1. The number of days it takes to sign up the library
2. The number of books the library can checkout per day, a library can only checkout books after it has been signed up
3. A list of book available for checkout in the library, with a unique ID

Also given a list of books ID with the corresponding point value

We only get N number of days to maximize the number of points we get from checking out books. A book only counts towards our total score ONCE, so checking the same book out from a single library or from different libraries is a waste of time. Each library can only checkout the given limit of books per day. We can checkout books from different libraries concurrently, however, we can only sign up libraries one at a time.

# First Attempt -  Monte Carlo (Random) Simulations:
We got this idea from our practice round. The practice round question was much simpler than the actually challenge, so in hindsight, this might not have been the best method (the availability bias lets us down yet again, but I digress). However the implementation was rather straightforward and it was a good starting point. Also, we did carry-over lots of ideas into our final solution.

Our method was: take the list of libraries and randomly sort them. Then start signing up the libraries in that random order. Furthermore, checkout the books from the library in the same random fashion.

Out initial attempt landed us a good number of points, probably around ~10M. We refined our random algorithm a bit further, and gained a bit more points. We filtered the initial list, before our random Monte Carlo simulations. We tried different filtering criteria, such as maximum potential value of the books in the library, shortest sign up dates, etc. By playing our our filtering, we managed to squeeze up to ~15M points out of the Monte Carlo method.

By this time, we were well into the challenge, probably half way through with 2 more hours to go. We saw that we were not getting much further, points wise, so we decided to switch gears.

# Second Attempt - Greedy Scheduling Algorithm:
Our second attempt was actually from the initial brainstorming we did before we tackled the MC simulations. From the question statement, most of us got a whiff of a scheduling question. Due to the fact we can only sign up a library one at a time, and also because we can only checkout books from a library after it has been signed up, this means that the order that we signed up the libraries was very important.

Now, almost everyone who has gone through an algorithms course in university has seen a few possible solution to the scheduling problem. So, without any surprise, our first attempt was a greedy approach. We decided to sign up the libraries in order of shortest sign up time first.

This proved to be a great initial heuristic as it landed up ~20M points. After this, we naturally played around with our sign up heuristic. We tried a few of them: maximum possible score from library first, most unique books in library first, etc.

We played around the heuristics, to the best that we could, although we soon hit a ceiling. (We ended up settle for the shortest sign up time first heuristic) We realized we probably needed to prune the dataset after each possible library is signed up, to avoid checkout books twice and adjust each libraries perceived value accordingly.

But playing with libraries was a costly operation. Trying to implement the filtering would be tricky, given the size of the data set (1,000 libraries, 100,000 to 1,000,000 unique library books). So instead of filtering the list and recalculating each libraries value, we settled for calculating a floating average for the dataset.  However, we calculated the average total possible point per library beforehand. And then, every single time, we calculated the average possible point of all the library, and we filtered the entire dataset by the top percentile. We tried and played around with the percentile: top 10%, top 20%, top 50%, top 75% and tried to get the maximum number of points.

With the greedy scheduling algorithm paired with the dataset pruning, we managed to finish with ~24.5M points. This brought us to the last few minutes of the contest, and we could not come up with any new ideas that was feasible in the time remaining.

Although this ranking was not high enough for us to advance to the final round, it was far better than we were expecting. We placed 2288th place globally, and 40th place in Canada.

This contest was a great learning experience and enjoyable contest for us all. We learned a lot about implementing real life solutions to real life problems. We learned that trying the easiest heuristic (greedy scheduling) is always a good first step and a random algorithm is probably not a good real life solution. And even though we did devote a lot of time in random MC simulation, that was not a total waste as we carried-over ideas into our final solution. Finally, we only found out at the end, but each dataset had some specific break down (for example some dataset had more library books than others, some datasets had shorter sign up time than others, etc.) and for next year we will definitely take these statistics into our tinkering. Overall, we were very happy with our result, have no regrets and are looking forward to competing again in 2021!
