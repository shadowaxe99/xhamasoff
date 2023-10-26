```javascript
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { updateDashboard } from '../redux/actions';

const Dashboard = () => {
  const dispatch = useDispatch();
  const dashboardData = useSelector(state => state.dashboardData);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetch('/get_recent_flags')
      .then(response => response.json())
      .then(data => {
        dispatch(updateDashboard(data));
        setIsLoading(false);
      })
      .catch(error => console.error('Error:', error));
  }, [dispatch]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div id="dashboard">
      <h2>Dashboard</h2>
      <div>
        <h3>Recent Flags</h3>
        {dashboardData.recentFlags.map((flag, index) => (
          <div key={index}>
            <p>{flag.tweet}</p>
            <p>{flag.decision}</p>
          </div>
        ))}
      </div>
      <div>
        <h3>Performance Metrics</h3>
        <p>Response Time: {dashboardData.performanceMetrics.responseTime}</p>
        <p>Accuracy: {dashboardData.performanceMetrics.accuracy}</p>
        <p>False Positives: {dashboardData.performanceMetrics.falsePositives}</p>
        <p>False Negatives: {dashboardData.performanceMetrics.falseNegatives}</p>
      </div>
    </div>
  );
};

export default Dashboard;
```