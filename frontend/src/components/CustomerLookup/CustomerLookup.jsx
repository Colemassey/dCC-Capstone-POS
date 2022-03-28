import React from "react";
import axios from "axios";



const CustomerLookup = (props) => {

    const [customers, setCustomers] = React.useState([]);

    React.useEffect(() => {
        getAllCustomer();
    }, []);
    
    async function getAllCustomer() {
        let response = await axios.get('http://127.0.0.1:8000/api/pos/customers/');
        setCustomers(response.data);
    };

    // async function handleEdit(requestBody) {
    //     const response = await axios.put(`http://127.0.0.1:8000/api/customers/${editingId}/`, requestBody).then((response)=> response).catch((error)=> console.log(error));  
    //     props.updateMusicLibrary(response) 
    // };
    
    return ( 
        <div>
            {customers.map((customer) => {
                        return (
                            <tbody key={customer.name}>
                                {console.log(customer.id)}
                                <tr>
                                    <th><large>{customer.first_name} {customer.last_name}</large></th>
                                </tr>
                                <tr>
                                    <td>{customer.address}</td>
                                </tr>
                                <tr>
                                    <td>{customer.phone_number}</td>
                                </tr>
                                </tbody>
            )})}
        </div>
     );
}

export default CustomerLookup;