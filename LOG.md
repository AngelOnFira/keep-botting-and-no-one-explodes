## Jan 9: Starting modules

I started by trying to implement a trivial module's logic, simple wires. I had to think of a way to structure files, so that any module can be generically called later. I'm going to put all of the modules into a module folder, but keep each separate in its own file. That way, one can be imported as follows:

`from modules.wires_simple import WiresSimple`

Next, I got testing set up. All the modules should be developed with Test Driven Development practices. Each module has its own discrete and explicit rules, and so creating test cases is pretty defined. Also, a solid testing suite will allow us to prevent regression on modules. Once we get to parsing the bomb with OpenCV, we should be confident that we don't have to debug modules there.

For testing, we are using pytest to write the tests, and Github Actions to test them every commit.
