```javascript
// Action Types
export const UPDATE_FEED = 'UPDATE_FEED';
export const UPDATE_DASHBOARD = 'UPDATE_DASHBOARD';
export const UPDATE_STATISTICS = 'UPDATE_STATISTICS';

// Action Creators
export const updateFeed = (newFeedData) => {
    return {
        type: UPDATE_FEED,
        payload: newFeedData
    }
}

export const updateDashboard = (newDashboardData) => {
    return {
        type: UPDATE_DASHBOARD,
        payload: newDashboardData
    }
}

export const updateStatistics = (newStatisticsData) => {
    return {
        type: UPDATE_STATISTICS,
        payload: newStatisticsData
    }
}
```