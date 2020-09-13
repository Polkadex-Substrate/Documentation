# Running Polkadex Proof of Concept Substrate Chain :test_tube:

## Introduction
We hope you have previously used Substrate and you are familiar with using it. This tutorial is not complete and will be improved as we build from the Proof of Concept to Stable verisons.
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
## Run the Node
1. Once it is compiled and run this command
    ``` ./target/release/node-polkadex --dev ```
2. You will start to see blocks getting generated. You can use the [polkadotapps](https://polkadot.js.org/apps/#/explorer) to interact with your local node
3. Currently you need to use the Alice key for sending transactions. You can see the current key in the settings
4. Go to Extrincis tab --> Generic Assets --> Create two new tokens for yourself. Note down the AssetIds emitted usually it will be "1" and "2".
5. Now you have minted yourself two tokens, Go to Dex pallet in the same extrinsics tab and choose registerOrderBook. Enter the trading_asset_id as "1" and base_asset_id as "2". 
6. Click Sign and Send. It will create a new orderbook in the dex pallet and registers their tokens pairs as you have given earlier. There will be event emitted by the transaction with the tradingPairId ( which will be 0 in this case).
7. No you can go to submitOrder and start placing orders.

NOTE: Price and Quantity is represented as FixedU128 (ie, if you want to enter 1.256 as your price. then enter the result of 1.256*(10^18)).
