>A simple smart contract to realize the voting function using Solidty.

**test procedure**

0.Install the **Ganache** and then open it, it will help you to create a local blockchain environment with some test nodes.


1.Go to the **Remix IDE** (https://remix.ethereum.org/), change the Remix IDE environment to **Web3 Provider**  and enter the Ganache default server address:HTTP://127.0.0.1:7545, then you can see node address list in your Remix page corresponds to your Ganache local environment. Next you can choose one address(which will be the constructor of the contract) to compile and deploy the smart contract **vote.sol**. 
  
 
 2.Use your constructor address(the address you use when you deploy the contract) to call the function **Give_right_to_voters** (only he has the right!)
  
   --I use python web3 library to do this, please check my **conn_test.ipynb**. You can also do it within Remix
 
 3.Copy the address of the contract you just deployed(can be found in 'Deployed Contracts' on Remix) and use it to replace the old address in **conn.py**.

 4.after doing all of above, you can run the flask app by entering following statements in your terminal:
 
  >export FLASK_APP=flask_app.py
  
  >flask run
 
 5.Then we can simulate voters vote via the browser.



