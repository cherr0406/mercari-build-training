import React, { useRef, useState } from 'react';

const server = process.env.REACT_APP_API_URL || 'http://127.0.0.1:9000';

interface Prop {
  onListingCompleted?: () => void;
}

type formDataType = {
  name: string;
  category: string;
  image: string | File;
};

export const Listing: React.FC<Prop> = (props) => {
  const { onListingCompleted } = props;
  const initialState = {
    name: '',
    category: '',
    image: '',
  };
  const [values, setValues] = useState<formDataType>(initialState);
  const inputFileRef = useRef<HTMLInputElement>(null);

  const handleFileBtnClick = () => {
    console.log('handleFileBtnClick');
    inputFileRef.current?.click();
  };

  const onValueChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setValues({
      ...values,
      [event.target.name]: event.target.value,
    });
  };
  const onFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setValues({
      ...values,
      [event.target.name]: event.target.files![0],
    });
  };
  const onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = new FormData();
    data.append('name', values.name);
    data.append('category', values.category);
    data.append('image', values.image);

    fetch(server.concat('/items'), {
      method: 'POST',
      mode: 'cors',
      body: data,
    })
      .then((response) => {
        console.log('POST status:', response.statusText);
        onListingCompleted && onListingCompleted();
      })
      .catch((error) => {
        console.error('POST error:', error);
      });
  };

  const displaySelectedFile = () => {
    if (!values.image) {
      return '選択されていません';
    } else if (values.image instanceof File) {
      return values.image.name;
    }
    return values.image;
  };

  return (
    <div className="Listing">
      <details open>
        <summary>出品する</summary>
        <form onSubmit={onSubmit} className="ListingForm btnripple3">
          <div className="ListingInput">
            <input
              type="text"
              name="name"
              id="name"
              placeholder="name"
              onChange={onValueChange}
              required
            />
            <input
              type="text"
              name="category"
              id="category"
              placeholder="category"
              onChange={onValueChange}
            />
            <div className="ListingFile">
              <button
                className="ListingFileButton"
                onClick={handleFileBtnClick}
              >
                ファイルを選択
              </button>
              <input
                type="file"
                name="image"
                id="image"
                ref={inputFileRef}
                onChange={onFileChange}
                required
              />
              <p>{displaySelectedFile()}</p>
            </div>
          </div>
          <button type="submit" className="ListingSubmitButton ShineAnime">
            List this item
          </button>
        </form>
      </details>
    </div>
  );
};
