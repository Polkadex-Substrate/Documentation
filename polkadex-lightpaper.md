![Logo](https://github.com/Polkadex-Substrate/Documentation/blob/master/images/Logo.svg)
## Abstract :memo:
We present a scalable, fully decentralized platform for exchanging tokens in a peer-peer and trustless manner. It enables high-frequency trading, high liquidity, and lightning-fast transaction speed for supporting Defi applications.
## Introduction
Substrate Blockchain Framework allows anyone to create application-specific blockchain without worrying about the technicality of block production and consensus.	It enables us to create a dedicated blockchain for decentralized exchange, which is purpose-built and configured to optimize the performance of DEXs. Previously Ethereum Smart Contracts allowed the creation of Defi services, but it is limited in computational resources required for the proper functioning of DEXs. It does not scale well. It is not upgradable, and it never provided a good trading experience, even after multiple hacks and catastrophic losses in the centralized exchanges like Mt. Gox, Bitfinex, etc. Orderbook based DEXs are not gaining volume. Limitations in computational resources led to the rise of Automated Market Making  (AMM) protocols like Uniswap. These protocols are profitable only when an arbitrage opportunity is available due to price differences in other exchanges. AMMs require Orderbook based exchanges, but Orderbook based exchanges do not require AMMs to function. 

We believe that AMMs can supplement Orderbook based DEXs combined with fast execution logic, three-second block time, custom trading bot support, and our unique feature -- On-Chain market making bots, a.k.a *"AMMs inside a DEX."* We present to you, Polkadex.

## Architecture :gear:
Polkadex's Design focuses on reducing the complexity of the chain. We believe that only those things that need public verifiability need to be on-chain. In Polkadex, Orderbook, Trader Assets Management, Bridge mechanism to Polkadot and Ethereum, and On-chain market making bots are On-Chain. Trading features like market data aggregation,  technical analysis indicators, storage and retrieval of trade history, and all the remaining exchange related features are made off-chain. It enabled us to increase the throughput of trades and made it comparable to the efficiency of centralized exchanges. 

Polkadex supports two types of trades, Limit and Market Orders. Market-taking orders have a trading fee of 0.2 percent, and market-making orders have zero trading fees. The market makers are incentivized by giving 50 percent of collected trading fees in their trades, and the remaining 50 percent is paid to Polkadex Team. Trading bots are economically impossible in smart contract-based DEXs due to high gas prices; we solve this by using zero network fees. In short, the market makers will get an extra 0.1 percent on their trades, and market takers pay 0.2 percent.

Polkadex does not collect network fees, a.k.a transaction fees. The Distributed Denial of Service (DDoS) problem associated with zero network fees can be solved if the blockchain can identify when getting attacked and charge network fees only for those attack transactions. Polkadex classifies each transaction as a good or potential DDoS attack, based on which network fees are levied from traders. Trades are classified as potential DDoS if the execution results in,
 

 - Invalid Price/Quantity Error 
 - Insufficient Balance 
 - Invalid Trading Pair 
 - Invalid Order type

Trading bots can use Market Data RPCs provided by the full nodes to retrieve market data for specific blocks. All technical analysis of market data can be done on the trader's side or the cloud. It also enables traders to use their custom trading algorithms and proprietary trading techniques.

The liquidity problem of order book based DEXs is solved by having On-Chain market making bots a.k.a AMMs inside the trading engine. Traders can provide liquidity for their favorite AMM curves like *constant product* AMMs. These AMMs acts like virtual market making bots hence called as On-Chain trading bots.
## On-Chain market making bots :robot:
Polkadex solves the problem of low liquidity by having AMMs directly connected to its trading engine. These AMMs act as On-Chain market making bots. When a trade is not matched against the Polkadex order book, the Polkadex Engine will check if these On-Chain trading bots can make an order that will match. The trades are executed only if a better price is provided by the On-Chain bots else it is inserted as a market-making order in the order book. It ensures that there is no price slippage problem for traders. In the first version, Polkadex will have a *constant product* market making bot.

More details will be updated later.
## Parachain to Polkadot :chains:
Polkadex provides two ways to bring liquidity, Polkadot Parachain and Snowfork trustless Ethereum Bridge. Polkadex parachain will have just one functionality to bridge liquidity to and from Polkadot to Polkadex. It will not have any other features. 

Polkadex Parachain allows traders to bring liquidity without trusting their assets with a centralized service or Polkadex Team, and Polkadot's interoperability layer secures all their assets.

##### References
* [Polkadot](https://polkadot.network/)
* [Learn more about Parachains](https://wiki.polkadot.network/docs/en/learn-parachains)
## Trustless Bridge: Snowfork :link:
Snowfork is a Substrate to Ethereum trustless bridge created by the Snowfork team. Once the Snowfork team completes the bridge, Polkadex will implement it; using Snowfork, traders can lock their assets on Ethereum using smart contracts and bridge liquidity to Polkadex. It does not involve any third parties, and assets are locked by the chain. Hence, trustless.

Polkadot Parachain and Snowfork's trustless bridge solves the problem of custody of funds in Polkadex. In short, traders do not need to worry about exchange getting hacked, and no-one else has custody of their funds.
## Polkadex Token Economics :chart:
Polkadex will have a total supply of *100 million tokens*. Initial Circulating Supply will be 10 million, out of which the Polkadex team will hold 6 million. The remaining 4 million tokens will be used to raise capital, ICO, and grants to teams that improve the Polkadex ecosystem.
The 90 million tokens will be released into circulation as block rewards to validators with an inflation rate of  I,

Where as, 

	0.025 < I < 0.1, where I depends on 0 < X< 1.0
* I = (Total supply at the end of the year – Total supply at the beginning of the year)/Total supply at the beginning of the year
* X = Total supply staked by validators and nominators(or traders)/ Total circulating supply.
## Roadmap :hourglass_flowing_sand:
- Q3 2020
    - Delivering Web3 Milestones
    - Documentation of Codebase
- Q4 2020
    - Testnet Launch
    - Parachain Implementation
- Q1 2020
    - Mainnet Launch
    - Security Audit
    - Public ICO
