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

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const usersEndpoint = useMemo(() => {
    if (process.env.REACT_APP_CODESPACE_NAME) {
      return `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
    }
    return 'http://localhost:8000/api/users/';
  }, []);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        console.log('Users endpoint:', usersEndpoint);
        const response = await fetch(usersEndpoint);
        if (!response.ok) {
          throw new Error('Failed to load users data.');
        }
        const data = await response.json();
        console.log('Users API response:', data);
        setUsers(normalizeListResponse(data));
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, [usersEndpoint]);

  if (loading) {
    return <p>Loading users...</p>;
  }

  if (error) {
    return <p className="text-danger">{error}</p>;
  }

  return (
    <div>
      <h2 className="h4 mb-3">Users</h2>
      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Alias</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.hero_alias}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Users;
