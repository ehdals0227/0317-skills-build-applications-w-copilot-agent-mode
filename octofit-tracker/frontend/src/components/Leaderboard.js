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

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const leaderboardEndpoint = useMemo(() => {
    if (process.env.REACT_APP_CODESPACE_NAME) {
      return `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    }
    return 'http://localhost:8000/api/leaderboard/';
  }, []);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        console.log('Leaderboard endpoint:', leaderboardEndpoint);
        const response = await fetch(leaderboardEndpoint);
        if (!response.ok) {
          throw new Error('Failed to load leaderboard data.');
        }
        const data = await response.json();
        console.log('Leaderboard API response:', data);
        setLeaderboard(normalizeListResponse(data));
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, [leaderboardEndpoint]);

  if (loading) {
    return <p>Loading leaderboard...</p>;
  }

  if (error) {
    return <p className="text-danger">{error}</p>;
  }

  return (
    <div>
      <h2 className="h4 mb-3">Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>User Email</th>
              <th>Points</th>
              <th>Rank</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry) => (
              <tr key={entry.id}>
                <td>{entry.id}</td>
                <td>{entry.user_email}</td>
                <td>{entry.points}</td>
                <td>{entry.rank}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
