import React from "react";
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';

import axios from "axios";
import useAuth from "../../hooks/useAuth";
import CustomerLookup from "../../components/CustomerLookup/CustomerLookup";

const HomePage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  const [user, token] = useAuth();

  // useEffect(() => {
  //   const fetchCars = async () => {
  //     try {
  //       let response = await axios.get("http://127.0.0.1:8000/api/cars/", {
  //         headers: {
  //           Authorization: "Bearer " + token,
  //         },
  //       });
  //       setCars(response.data);
  //     } catch (error) {
  //       console.log(error.message);
  //     }
  //   };
  //   fetchCars();
  // }, [token]);

  return (
    <div className="container">
      <h1>{user.username}</h1>
      <div>
      <TabContext>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <TabList>
            <Tab label="Customer Lookup" value="1" />
            <Tab label="Sizes" value="2" />
            <Tab label="Toppings" value="3" />
            <Tab label="Sides" value="4" />
            <Tab label="Drinks" value="5" />
            <Tab label="Orders" value="6" />
          </TabList>
        </Box>
        <TabPanel index="1"><CustomerLookup /></TabPanel>
        <TabPanel value="2">Toppings</TabPanel>
        <TabPanel value="3">Item Three</TabPanel>
        <TabPanel value="4">Item Three</TabPanel>
        <TabPanel value="5">Item Three</TabPanel>
        <TabPanel value="6">Item Three</TabPanel>
      </TabContext>
      </div>
    </div>
  );
};

export default HomePage;
