class Badge {
    public String print(Integer id, String name, String department) {
        String dept = (department != null) ? department.toUpperCase() : "OWNER";

        if (id != null) {
            return String.format("[%s] - %s - %s", id, name, dept);
        } else {
            return String.format("%s - %s", name, dept);
        }
    }
}
