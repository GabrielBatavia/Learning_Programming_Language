
//make a array object

// Step 1: Definisi kelas Student
public class persiapan_uts_smstr2 {
    // Atribut untuk nama dan usia
    private String name;
    private int age;

    // Konstruktor untuk kelas Student
    public persiapan_uts_smstr2(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Metode toString untuk mencetak informasi siswa
    public String toString() {
        return "Student{Name: " + name + ", Age: " + age + "}";
    }

    public static void main(String[] args) {
        // Step 2: Membuat objek dari kelas Student
        persiapan_uts_smstr2 student1 = new persiapan_uts_smstr2("Alice", 20);
        persiapan_uts_smstr2 student2 = new persiapan_uts_smstr2("Bob", 22);
        persiapan_uts_smstr2 student3 = new persiapan_uts_smstr2("Charlie", 19);

        // Step 3: Membuat array of objects
        persiapan_uts_smstr2[] students = new persiapan_uts_smstr2[3];
        students[0] = student1;
        students[1] = student2;
        students[2] = student3;

        // Menampilkan semua siswa menggunakan loop
        for (persiapan_uts_smstr2 student : students) {
            System.out.println(student);
        }

        // Membuat array of object baru menggunakan for loop
        persiapan_uts_smstr2[] murid = new persiapan_uts_smstr2[jumlah_Murid]
    }
}