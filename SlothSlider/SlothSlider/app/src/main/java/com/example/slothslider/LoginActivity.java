package com.example.slothslider;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;
public class LoginActivity extends AppCompatActivity {

    private EditText editTextEmail, editTextPassword;
    private FirebaseAuth mAuth;
    private Intent intent;
    private Activity activity = this;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        mAuth = FirebaseAuth.getInstance();

        editTextEmail= findViewById(R.id.email);
        editTextPassword = findViewById(R.id.password);

        Button buttonLogin = findViewById(R.id.IniciarSesion);

        buttonLogin.setOnClickListener (v -> iniciarSesion());

        Button buttonRegistro = findViewById(R.id.CrearCuenta);

        buttonRegistro.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(activity, RegisterActivity.class);
                activity.startActivity(intent);
            }
        });
        //buttonRegistro.setOnClickListener(startActivity(new Intent(LoginActivity.this,RegisterActivity.class)));


    }

    private void iniciarSesion(){
        String email = editTextEmail.getText().toString().trim();
        String password = editTextPassword.getText().toString().trim();

        //Validaciones de los campos:

        mAuth.signInWithEmailAndPassword(email,password)
                .addOnCompleteListener(this, task -> {
                    if(task.isSuccessful()){
                        //Inicio de sesión exitoso, navegar a la pantalla principal
                        startActivity(new Intent(LoginActivity.this, HomeActivity.class));
                        finish();
                    }else{
                        // Error al iniciar sesión

                        Toast.makeText(LoginActivity.this, "Error al iniciar sesión: "
                        + task.getException().getMessage(),Toast.LENGTH_SHORT).show();
                    }
                });
    }
}
