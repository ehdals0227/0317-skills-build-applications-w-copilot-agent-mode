import { useEffect, useMemo, useState } from 'react';

const normalizeListResponse = (payload) => {
  if (Array.isArray(payload)) {
    return payload;
  }
  if (payload && Array.isArray(payload.results)) {
    return payload.results;
  }
  return [];
};

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const activitiesEndpoint = useMemo(() => {
    if (process.env.REACT_APP_CODESPACE_NAME) {
      return `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    }
    return 'http://localhost:8000/api/activities/';
  }, []);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        console.log('Activities endpoint:', activitiesEndpoint);
        const response = await fetch(activitiesEndpoint);
        if (!response.ok) {
          throw new Error('Failed to load activities data.');
        }
        const data = await response.json();
        console.log('Activities API response:', data);
        setActivities(normalizeListResponse(data));
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchActivities();
  }, [activitiesEndpoint]);

  if (loading) {
    return <p>Loading activities...</p>;
  }

  if (error) {
    return <p className="text-danger">{error}</p>;
  }

  return (
    <div>
      <h2 className="h4 mb-3">Activities</h2>
      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>User Email</th>
              <th>Type</th>
              <th>Duration (min)</th>
              <th>Calories</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity) => (
              <tr key={activity.id}>
                <td>{activity.id}</td>
                <td>{activity.user_email}</td>
                <td>{activity.activity_type}</td>
                <td>{activity.duration_minutes}</td>
                <td>{activity.calories_burned}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
