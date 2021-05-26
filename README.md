>A simple smart contract to realize the voting function using Solidty.

**test procedure**

1.Within the **Remix**  compile and deploy my smart contract. 
  
  --If you want to test with ganache, you should change the Remix IDE environment to **Web3 Provider**  with the ganache default server address:HTTP://127.0.0.1:7545, then you can see address list in your Remix page corresponds to your Ganache local environment.
 

 2.Use your constructor address(the address you use when you delpoy the contract) to call the function **Give_right_to_voters**  
  
   --I use python web3 library to do this, please check my conn_test.ipynb. You can also do it within Remix
 
 3.Copy the deployed contract address(can be found in 'Deployed Contracts' in Remix) and use it to replace the address in conn.py.

 4.Run the flask app by entering following statements in your terminal:
 
  >export FLASK_APP=flask_app.py
  
  >flask run
 
 5.then we can simulate voters vote via the browser.



