
# Polkadex trading documentation

## Overview

In this documentation we intend to provide an overview of how to start the blockchain and place the following type of trades and observe these changes in the blockchain data.

 1. Bid limit
 2. Ask limit
 3. Bid Market
 4. Ask Market

# Start the blockchain

Once you have compiled the source code, run the following command to start the blockchain,

    ~/Polkadex/target/release/node-polkadex --dev

If you are test running it for the second time, be sure to delete the old database by using the following command,

    ~/Polkadex/target/release/node-polkadex purge-chain --dev

# Setting up the browser

To test the different type of trades, please open the following link in the local browser:

https://polkadot.js.org/apps/#/explorer

To connect to the local testnet, you need to change the source database to localhost, as given in the following image:

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image001.png)

Clicking on the above link will help you select the local node:

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image003.png)

You will now start seeing the blocks getting generated:

![image005](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image005.jpg)

# Terminal view

You can also verify it from the terminal. You should see something similar:

![image007](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image007.jpg)

# View the blockchain state

To view the chain state and the numbers entered during the trade, please click the below link,

![image009](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image009.jpg)

# Interact with blockchain and submit orders

To submit orders and to interact with the blockchain database, click on the below link,

![image011](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image011.jpg)

# Create an asset

Go to [https://polkadot.js.org/apps/#/extrinsics](https://polkadot.js.org/apps/#/extrinsics), select ‘genericAsset’, choose ‘create’ function and submit transaction as given below. Please make sure you select the “Milliunit” because of certain issues with the default javascript interface.

![image013](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image013.jpg)

Click on ‘sign and submit’

![image015](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image015.jpg)

Verify using the blockchain explorer link,

![image017](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image017.jpg)

# Create an orderbook of two assets

Choose ‘polkadex’ pallet from the extrinsics and choose the ‘registerNewOrderbook’ function and choose the desired assets:

![image019](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image019.jpg)

Verify on the main page and note down the hash of the new orderbook created. In the example below,

_0xf28a3c76161b8d5723b6b8b092695f418037c747faa2ad8bc33d8871f720aac9_

![image021](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image021.jpg)

# Submit a bid limit order

Select the user, extrinsic type, submitOrder function, order type, the hash of the orderbook, price and quantity. Please make sure you select the “Milliunit” because of certain issues with the default javascript interface.

![image023](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image023.jpg)

# Submit an ask limit order

Select the user, extrinsic type, submitOrder function, order type, the hash of the orderbook, price and quantity. Please make sure you select the “Milliunit” because of certain issues with the default javascript interface.

![image025](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image025.jpg)

# View free balance and reserve balance

Go to ‘chain state’ and select the ‘selected state query’ as ‘genericAsset’ and the required asset type from the tab. In the asset ID, select the asset you want to view for the user. Click on the ‘+’ button.

![image027](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image027.jpg)

![image029](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image029.jpg)

# View Ask levels, bid levels in the created orderbook

 1. In the ‘chain state’ page, select the ‘state query’ as Polkadex and choose the corresponding database. 
 2. Enter the hash of the corresponding orderbook.

![image031](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image031.jpg)

# Submit a bid market order

Repeat the same step as ‘Bid Limit’ but select the order type as ‘BidMarket’ and make sure we give the price alone and leave the quantity as blank.

![image033](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image033.jpg)

# Submit an ask market order

Repeat the same step as ‘Ask Limit’ but select the order type as ‘AskMarket’ and make sure we give the quantity alone and leave the price as blank.

![image035](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/clip_image035.jpg)
