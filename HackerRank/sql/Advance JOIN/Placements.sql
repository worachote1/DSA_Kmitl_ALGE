SELECT
    st.Name
FROM Students st
JOIN Friends f
    ON st.ID = f.ID
JOIN Packages pst
    ON st.ID = pst.ID
JOIN Packages pf
    ON f.Friend_ID = pf.ID
WHERE pst.Salary < pf.Salary
ORDER BY
    pf.Salary