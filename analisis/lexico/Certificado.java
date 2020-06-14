/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fes.aragon.entidades;

/**
 *
 * @author crist
 */
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
        return certificado; //To change body of generated methods, choose Tools | Templates.
    }
    
}
