```javascript
import { UPDATE_FEED, UPDATE_DASHBOARD, UPDATE_STATISTICS } from './actions';

const initialState = {
  feed: [],
  dashboard: {},
  statistics: {}
};

function feedReducer(state = initialState.feed, action) {
  switch (action.type) {
    case UPDATE_FEED:
      return action.payload;
    default:
      return state;
  }
}

function dashboardReducer(state = initialState.dashboard, action) {
  switch (action.type) {
    case UPDATE_DASHBOARD:
      return action.payload;
    default:
      return state;
  }
}

function statisticsReducer(state = initialState.statistics, action) {
  switch (action.type) {
    case UPDATE_STATISTICS:
      return action.payload;
    default:
      return state;
  }
}

export default function rootReducer(state = initialState, action) {
  return {
    feed: feedReducer(state.feed, action),
    dashboard: dashboardReducer(state.dashboard, action),
    statistics: statisticsReducer(state.statistics, action)
  };
}
```