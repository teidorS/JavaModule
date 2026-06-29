class Badge {
    public String print(Integer id, String name, String department) {
        String dept = (department != null) ? department.toUpperCase() : "OWNER";

        if (id != null) {
            return "[" + id + "] - " + name + " - " + dept;
        } else {
            return name + " - " + dept;
        }
    }
}
