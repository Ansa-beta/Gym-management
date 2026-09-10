import streamlit as st
from gym_views import DbConnect,GymMemberManager
connection_instance=DbConnect()
member_instance=GymMemberManager()

tab1,tab2=st.tabs(["ADD","VIEW"])
with tab1:
    st.title("Add new gym member")
    name=st.text_input("Enter member name: ")
    place=st.text_input("Enter place: ")
    mobile_no=st.text_input("Enter mobile number: ")
    plan=st.text_input("Enter plan: ")
    fee=st.text_input("Enter fee: ")
    joined_date=st.text_input("Enter joined date: ")
    if st.button("Add new member"):
        member_instance.post(name=name,place=place,mobile_no=mobile_no,plan=plan,fee=fee,joined_date=joined_date)
        st.success("New member added successfully!!!")
with tab2:
    st.title("View gym member details")
