# Running Polkadex Chain (Beta):test_tube:

## Overview
In this documentation we intend to provide an overview of how to start the blockchain and place the following type of trades and observe these changes in the blockchain data.

 1. Bid limit
 2. Ask limit
 3. Bid Market
 4. Ask Market
## Prerequisites
You will probably need to do some set-up to prepare your computer for Substrate development.
1. If you are using a Unix-based machine (Linux, MacOS), we have created a simple one-liner to help you set up your computer
    ``` curl https://getsubstrate.io -sSf | bash -s -- --fast ```
## Compile
1. Clone the [Polkadex](https://github.com/Polkadex-Substrate/Polkadex.git) repository.
2. Initialize the WebAssembly Environment
    ```
    # Load settings into the current shell script if you can't use rustup command
    # If you've run this before, you don't need to run it again. But doing so is harmless.
    source ~/.cargo/env

    # Update Rust
    rustup update nightly
    rustup update stable

    # Add Wasm target
    rustup target add wasm32-unknown-unknown --toolchain nightly
    ```
3. Change directory and Compile the Polkadex Chain
   ```
   cd polkadex/
   cargo build --release
   ```
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

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image005.png)

# Terminal view

You can also verify it from the terminal. You should see something similar:

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image007.png)

# View the blockchain state

To view the chain state and the numbers entered during the trade, please click the below link,

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image009.png)

# Interact with blockchain and submit orders

To submit orders and to interact with the blockchain database, click on the below link,

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image011.png)

# Create an asset

Go to [https://polkadot.js.org/apps/#/extrinsics](https://polkadot.js.org/apps/#/extrinsics), select ‘genericAsset’, choose ‘create’ function and submit transaction as given below. Please make sure you select the “Milliunit” because of certain issues with the default javascript interface.

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image013.png)

Click on ‘sign and submit’

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image015.png)

Verify using the blockchain explorer link,

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image017.png)

# Create an orderbook of two assets

Choose ‘polkadex’ pallet from the extrinsics and choose the ‘registerNewOrderbook’ function and choose the desired assets:

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image019.png)

Verify on the main page and note down the hash of the new orderbook created. In the example below,

_0xf28a3c76161b8d5723b6b8b092695f418037c747faa2ad8bc33d8871f720aac9_

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image021.png)

# Submit a bid limit order

Select the user, extrinsic type, submitOrder function, order type, the hash of the orderbook, price and quantity. Please make sure you select the “Milliunit” because of certain issues with the default javascript interface.

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image023.png)

# Submit an ask limit order

Select the user, extrinsic type, submitOrder function, order type, the hash of the orderbook, price and quantity. Please make sure you select the “Milliunit” because of certain issues with the default javascript interface.

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image025.png)

# View free balance and reserve balance

Go to ‘chain state’ and select the ‘selected state query’ as ‘genericAsset’ and the required asset type from the tab. In the asset ID, select the asset you want to view for the user. Click on the ‘+’ button.

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image027.png)

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image029.png)

# View Ask levels, bid levels in the created orderbook

 1. In the ‘chain state’ page, select the ‘state query’ as Polkadex and choose the corresponding database. 
 2. Enter the hash of the corresponding orderbook.

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image031.png)

# Submit a bid market order

Repeat the same step as ‘Bid Limit’ but select the order type as ‘BidMarket’ and make sure we give the price alone and leave the quantity as blank.

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image033.png)

# Submit an ask market order

Repeat the same step as ‘Ask Limit’ but select the order type as ‘AskMarket’ and make sure we give the quantity alone and leave the price as blank.

![](https://raw.githubusercontent.com/Polkadex-Substrate/Documentation/master/images/clip_image035.png)
