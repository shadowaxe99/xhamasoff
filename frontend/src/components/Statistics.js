```javascript
import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';

const Statistics = () => {
  const [statistics, setStatistics] = useState({
    totalTweets: 0,
    realEvents: 0,
    fakeEvents: 0,
    falsePositives: 0,
    falseNegatives: 0,
  });

  const updateStatistics = useSelector(state => state.updateStatistics);

  useEffect(() => {
    setStatistics({
      totalTweets: updateStatistics.totalTweets,
      realEvents: updateStatistics.realEvents,
      fakeEvents: updateStatistics.fakeEvents,
      falsePositives: updateStatistics.falsePositives,
      falseNegatives: updateStatistics.falseNegatives,
    });
  }, [updateStatistics]);

  return (
    <div id="statistics">
      <h2>Statistics</h2>
      <p>Total Tweets Monitored: {statistics.totalTweets}</p>
      <p>Real Events: {statistics.realEvents}</p>
      <p>Fake Events: {statistics.fakeEvents}</p>
      <p>False Positives: {statistics.falsePositives}</p>
      <p>False Negatives: {statistics.falseNegatives}</p>
    </div>
  );
};

export default Statistics;
```