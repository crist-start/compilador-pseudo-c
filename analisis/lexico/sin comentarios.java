
package fes.aragon.entidades;


public class Certificado {
    private int llave_certificado;
    private String certificado;

    public Certificado() {
    }

    public Certificado(int llave_certificado, String certificado) {
        this.llave_certificado = llave_certificado;
        this.certificado = certificado;
    }

    public String getCertificado() {
        return certificado;
    }

    public void setCertificado(String certificado) {
        this.certificado = certificado;
    }

    public int getLlave_certificado() {
        return llave_certificado;
    }

    public void setLlave_certificado(int llave_certificado) {
        this.llave_certificado = llave_certificado;
    }

    @Override
    public String toString() {
        return certificado; 
    }
    
}
