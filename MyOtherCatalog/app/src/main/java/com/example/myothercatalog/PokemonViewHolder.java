package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class PokemonViewHolder extends RecyclerView.ViewHolder{
    private final TextView textView;
    private final ImageView imageView;
    private Button button;
    public PokemonViewHolder (@NonNull View itemView){
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.pokemon_name_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.pokemon_image_view);
        button = itemView.findViewById(R.id.button);
    }
    public void showData(PokemonData data, Activity activity){
        textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into (imageView);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Context context = view.getContext();

                Intent intent = new Intent(context, DetailActivity.class);

                context.startActivity(intent);
            }
        });
    }

}
