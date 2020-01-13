## Jan 9: Starting modules

### By Forest

I started by trying to implement a trivial module's logic, simple wires. I had to think of a way to structure files, so that any module can be generically called later. I'm going to put all of the modules into a module folder, but keep each separate in its own file. That way, one can be imported as follows:

`from modules.wires_simple import WiresSimple`

Next, I got testing set up. All the modules should be developed with Test Driven Development practices. Each module has its own discrete and explicit rules, and so creating test cases is pretty defined. Also, a solid testing suite will allow us to prevent regression on modules. Once we get to parsing the bomb with OpenCV, we should be confident that we don't have to debug modules there.

For testing, we are using pytest to write the tests, and Github Actions to test them every commit.

## Jan 13: Working on testing system

### By Forest

It's best to keep certain sections of the codebase separate. The bomb analysis, bomb movement, and module solving systems should all be isolated. Because of this, we can also detach logic testing from game control testing.

Logic testing is the easiest to start off with. It can be implemented with only a few if statements. Setting up testing around it allows us to make sure that the testing system can scale painlessly. One of the big concerns is how to pass test data back.

Originally, I thought that it would be best for the logic systems to execute the solution on the bomb. A module's logic class could keep information like where to click with certain conditions. Hoever, this doesn't decouple systems as nicely. On top of that, it would be hard to test as it wouldn't explicitly return the logic system's solution. It would have to be captured with capsys, which captures any system out. This isn't ideal.

Any logic modules now return a solution that can be interpreted by an execution system for the model. This will hold all of the instruction on how a logic module's solution should be executed. Now tests can easily assert their expected result against what was returned.
