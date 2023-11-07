package com.example.mycatalog;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class CatalogActivity extends AppCompatActivity {
    //Aquí inicializamos las variables boton que es de tipo boton y context
    private Button boton;
    private Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.catalog_activity);
        //Aquí lo que hacemos es que la variable que inicializamos antes tenga las propiedades que pusimos en el xml, para ello
        // usamos el findViewById y ponemor la id que le dimos en el xml
        boton = findViewById(R.id.boton1);
        // A partir de aquí lo que hacemos es que cuando el usuario pulse el botón se inicie la clase DetailActivity
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(context, DetailActivity.class);
                context.startActivity(intent);
            }
        });
    }
}
