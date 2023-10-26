```javascript
import React from 'react';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import rootReducer from './redux/reducers';
import Dashboard from './components/Dashboard';
import Feed from './components/Feed';
import Statistics from './components/Statistics';

const store = createStore(rootReducer);

function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <Dashboard />
        <Feed />
        <Statistics />
      </div>
    </Provider>
  );
}

export default App;
```