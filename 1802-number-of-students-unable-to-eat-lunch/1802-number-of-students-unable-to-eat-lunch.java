class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int res = students.length;
        HashMap<Integer, Integer> dict1 = new HashMap<>();

        for (int student : students) {
            dict1.put(student, dict1.getOrDefault(student, 0) + 1);
        }

        for (int s : sandwiches) {
            if (dict1.getOrDefault(s, 0) > 0) {
                res--;
                dict1.put(s, dict1.get(s) - 1);
            } else {
                break;
            }
        }

        return res;
    }
}