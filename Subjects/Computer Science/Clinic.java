public class Clinic {
  public class PersegiPanjang {
    public double hitungKeliling(int panjang, int lebar) {
      return 2 * (panjang + lebar);
    }
    public double hitungLuas(int panjang, int lebar) {
      return panjang * lebar;
    }
  }

  public class Persegi {
    private int sisi;

    public Persegi(int sisi) {
      this.sisi = sisi;
    }

    public double getSisi() {
      return this.sisi;
    }

    public double hitungLuas() {
      return sisi * sisi;
    }
    public double hitungKeliling() {
      return 4 * sisi;
    }
  }

  private void solve() {
    Persegi pa = new Persegi(5);
    Persegi pb = new Persegi(8);
    Persegi pc = new Persegi(13);

    System.out.println("Persegi dengan panjang sisi " + pa.getSisi());
    System.out.println("Luas: " + pa.hitungLuas());
    System.out.println("Keliling: " + pa.hitungKeliling());
    System.out.println();

    System.out.println("Persegi dengan pbnjang sisi " + pb.getSisi());
    System.out.println("Luas: " + pb.hitungLuas());
    System.out.println("Keliling: " + pb.hitungKeliling());
    System.out.println();

    System.out.println("Persegi dengan pcnjang sisi " + pc.getSisi());
    System.out.println("Luas: " + pc.hitungLuas());
    System.out.println("Keliling: " + pc.hitungKeliling());
    System.out.println();

    // Argument

    PersegiPanjang pj = new PersegiPanjang();
    System.out.println("Luas persegi panjang 6x9: " + pj.hitungLuas(6, 9));
    System.out.println("Keliling persegi panjang 4x2: " + pj.hitungKeliling(4, 2));
  }

	public static void main(String... args) {
    Clinic main = new Clinic();
    main.solve();
  }
}
