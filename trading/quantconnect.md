One of our primary development platforms at Quant SC has been QuantConnect. It
provides:
1. Easy access to market data (fundamental data, options contracts,
pricing data)
2. Backtesting, paper trading, and live trading capabilities
3. A fairly robust community forum with answers to different internal tools'
bugs and sample implementations of different algorithms
4. A Jupyter notebook environment for data analysis and testing

### Basic Algorithm Framework
1. Initialize your program
  - For backtesting, start and end dates can be specified to help expedite
  tests if you're interested only in a certain range of data.
    - Note that the further back you go, the less data may be available
  - Starting capital must be set so that you are able to make trades
  - Scheduling functions can be used to perform routine functions
2. Select a universe
  - A universe is a group of assets that you are thinking about trading
  - Universe selection can be performed on a routine basis using flagging
3. Create a trading signal
  - Some logic to determine which elements of a universe should be traded should
  exist. The trading signal's 'advice' will likely fluctuate with new data and
  thus be re-acquired/calculated as time progresses
4. Construct a portfolio
  - Once a trading signal exists (i.e. you have some metric informing the
    trades you want to make on assets in your universe), it should be used to
    finalize the decisions about which assets you want to trade and how.
  - Different concentrations of your portfolio may be allocated for different
  positions
5. Create an execution method to achieve the portfolio target
  - Once you have a target portfolio, you need to execute the trades to actually
  attain it
  - SetHoldings, MarketOrder, LimitOrder, StopMarketOrder, StopLimitOrder,
  MarketOnOpenOrder, and MarketOnCLoseOrder are all options for acquiring assets
  -
6. Manage Risk
  - A trading strategy should have some logic to liquidate elements of a
  portfolio as necessary to reduce losses (think trailing stops) and increase
  profits (recalibrating with the trading signal)
  - SetHoldings conveniently allows rebalancing of a position to a certain
  proportion of your portfolio size
  - Liquidate allows for you to get rid of your position in a specific ticker or
  across all tickers

### Further Reading
QuantConnect offers tutorials that you will be prompted with once you create an
account.
QuantConnect also provides documentation on their functions, which can be found
at https://www.quantconnect.com/docs/home/home
