import { useEffect, useState } from "react";

function Profile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
  const token = localStorage.getItem("token");

  const res = await fetch("http://127.0.0.1:8000/profile/me", {
    headers: {
      Authorization: "Bearer " + token,
    },
  });

  const data = await res.json(); // ✅ must come first

  if (!res.ok) {
    console.log("Error:", data);
    return;
  }

  console.log("Profile:", data);
  setProfile(data);
};

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.reload();
    };

  return (
    <div>
      <h2>My Profile</h2>

      {profile ? (
        <div>
          <p>Name: {profile.name}</p>
          <p>Age: {profile.age}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}

      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Profile;